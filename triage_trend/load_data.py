import pandas as pd

def load_data():
    weather_features_path = 'data/weather_features.csv'
    weather_df = pd.read_csv(weather_features_path)

    moon_path = 'data/moon_phase.csv'
    moon_df = pd.read_csv(moon_path)

    vacations_path = 'data/vacations.csv'
    vacations_df = pd.read_csv(vacations_path)

    new_data_path = 'data/clienia_dataset.csv'  # Adjust this path as needed
    new_df = pd.read_csv(new_data_path)

    # Ensure datetime formats
    weather_df['Datum'] = pd.to_datetime(weather_df['Datum'])
    moon_df['Date'] = pd.to_datetime(moon_df['Date'])
    vacations_df['Date'] = pd.to_datetime(vacations_df['Date'])
    new_df['Fall_Eintritt_Datum'] = pd.to_datetime(new_df['Fall_Eintritt_Datum'], format='%m/%d/%y')

    # Timezone normalization
    weather_df['Datum'] = weather_df['Datum'].dt.tz_localize(None)

    # Merging datasets
    combined_df = pd.merge(weather_df, moon_df, left_on='Datum', right_on='Date', how='inner')
    combined_df.drop(columns=['Date'], inplace=True)
    combined_df = pd.merge(combined_df, vacations_df, left_on='Datum', right_on='Date', how='left')
    combined_df.drop(columns=['Date'], inplace=True)

    # Count occurrences
    date_counts = new_df['Fall_Eintritt_Datum'].value_counts().reset_index()
    date_counts.columns = ['Datum', 'Date_Occurrences']
    combined_df = pd.merge(combined_df, date_counts, on='Datum', how='left')
    combined_df['Date_Occurrences'] = combined_df['Date_Occurrences'].fillna(0).astype(int)

    # Weekday
    combined_df['Weekday'] = combined_df['Datum'].dt.day_name()

    return combined_df
