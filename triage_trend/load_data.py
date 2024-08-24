import pandas as pd


def load_data():
    # Load existing datasets
    weather_features_path = "data/weather_features.csv"
    weather_df = pd.read_csv(weather_features_path)

    moon_path = "data/moon_phase.csv"
    moon_df = pd.read_csv(moon_path)

    vacations_path = "data/vacations.csv"
    vacations_df = pd.read_csv(vacations_path)

    new_data_path = "data/clienia_dataset.csv"  # Adjust this path as needed
    new_df = pd.read_csv(new_data_path)

    public_holidays_path = "data/public_holidays.csv"
    public_holidays_df = pd.read_csv(public_holidays_path)

    # Ensure datetime formats
    weather_df["Datum"] = pd.to_datetime(weather_df["Datum"])
    moon_df["Date"] = pd.to_datetime(moon_df["Date"])
    vacations_df["Date"] = pd.to_datetime(vacations_df["Date"])
    new_df["Fall_Eintritt_Datum"] = pd.to_datetime(
        new_df["Fall_Eintritt_Datum"], format="%m/%d/%y"
    )
    public_holidays_df["Date"] = pd.to_datetime(public_holidays_df["Date"])

    # Timezone normalization
    weather_df["Datum"] = weather_df["Datum"].dt.tz_localize(None)

    # Merging datasets
    combined_df = pd.merge(
        weather_df, moon_df, left_on="Datum", right_on="Date", how="inner"
    )
    combined_df.drop(columns=["Date"], inplace=True)
    combined_df = pd.merge(
        combined_df, vacations_df, left_on="Datum", right_on="Date", how="left"
    )
    combined_df.drop(columns=["Date"], inplace=True)

    # Merge with public holidays dataset
    combined_df = pd.merge(
        combined_df,
        public_holidays_df,
        left_on="Datum",
        right_on="Date",
        how="left",
    )
    combined_df.drop(columns=["Date"], inplace=True)

    # Count occurrences
    date_counts = new_df["Fall_Eintritt_Datum"].value_counts().reset_index()
    date_counts.columns = ["Datum", "Date_Occurrences"]
    combined_df = pd.merge(combined_df, date_counts, on="Datum", how="left")
    combined_df["Date_Occurrences"] = (
        combined_df["Date_Occurrences"].fillna(0).astype(int)
    )

    # Weekday
    combined_df["Weekday"] = combined_df["Datum"].dt.day_name()

    combined_df = add_holiday_and_weather_features(combined_df)

    combined_df.to_csv("tempdata.csv")

    return combined_df


def add_holiday_and_weather_features(df):
    """Add features for holiday periods and 5-day rolling mean for weather data."""
    # Holiday-related features for each canton
    cantons = [
        "Aargau",
        "Zug",
        "Schwyz",
        "St_gallen",
        "Schaffhausen",
        "Thurgau",
        "Zurich",
    ]

    for canton in cantons:
        holiday_col = f"IsVacation{canton}"

        if holiday_col in df.columns:
            # Identify the week after a holiday ends (when the holiday switches from 1 to 0)
            df[f"{canton}_Week_After_Holiday"] = (
                (df[holiday_col] == 0) & (df[holiday_col].shift(7) == 1)
            ).astype(int)

            # Identify the first week of the holiday (when the holiday switches from 0 to 1)
            df[f"{canton}_First_Week_of_Holiday"] = (
                (df[holiday_col] == 1) & (df[holiday_col].shift(7) == 0)
            ).astype(int)
        else:
            # If the holiday column doesn't exist, fill with zeros
            df[f"{canton}_Week_After_Holiday"] = 0
            df[f"{canton}_First_Week_of_Holiday"] = 0

    # Compute 5-day rolling means for weather-related features
    weather_columns = [
        "Average_Temperature",
        "Max_Temperature",
        "Total_Rain_Duration",
        "Average_Pressure",
        "Average_Global_Radiation",
        "Cloudiness",
    ]

    df.set_index("Datum", inplace=True)
    df_rolling_means = (
        df[weather_columns].rolling(window=5).mean().shift(1)
    )  # 5-day rolling means, shift to previous day
    df = df.join(df_rolling_means, rsuffix="_5day_mean")

    # Reset index after joining
    df.reset_index(inplace=True)

    return df
