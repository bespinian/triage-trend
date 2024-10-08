import os

import joblib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from triage_trend.load_data import load_data

CATEGORICAL_COLUMNS = ["Weekday"]
NUMERIC_COLUMNS = [
    "Average_Temperature",
    "Max_Temperature",
    "Total_Rain_Duration",
    "Average_Pressure",
    "Average_Global_Radiation",
    "Cloudiness",
    "Moon Phase (%)",
    "IsVacationAargau",
    "IsVacationZug",
    "IsVacationSchwyz",
    "IsVacationSt_gallen",
    "IsVacationSchaffhausen",
    "IsVacationThurgau",
    "Aargau_Week_After_Holiday",
    "Aargau_First_Week_of_Holiday",
    "Zug_Week_After_Holiday",
    "Zug_First_Week_of_Holiday",
    "Schwyz_Week_After_Holiday",
    "Schwyz_First_Week_of_Holiday",
    "St_gallen_Week_After_Holiday",
    "St_gallen_First_Week_of_Holiday",
    "Schaffhausen_Week_After_Holiday",
    "Schaffhausen_First_Week_of_Holiday",
    "Thurgau_Week_After_Holiday",
    "Thurgau_First_Week_of_Holiday",
    "Average_Temperature_5day_mean",
    "Max_Temperature_5day_mean",
    "Total_Rain_Duration_5day_mean",
    "Average_Pressure_5day_mean",
    "Average_Global_Radiation_5day_mean",
    "Cloudiness_5day_mean",
    "publicHolidayAargau",
    "publicHolidayZug",
    "publicHolidaySchwyz",
    "publicHolidayStGallen",
    "publicHolidayThurgau",
    "publicHolidaySchaffhausen",
    "publicHolidayZurich",
]


def map_weekdays(df):
    weekday_mapping = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6,
    }
    df["Weekday"] = df["Weekday"].map(weekday_mapping)
    return df


def handle_missing_values(df):
    numeric_cols = df.select_dtypes(include=["number"]).columns.drop(
        "Date_Occurrences"
    )
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    for col in CATEGORICAL_COLUMNS:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df


def preprocess_data(df):
    df = map_weekdays(df)
    df = handle_missing_values(df)

    df["IsWeekend"] = df["Weekday"].isin([5, 6]).astype(int)

    df = df.select_dtypes(exclude=["datetime64"])
    X = df.drop(columns=["Date_Occurrences"])
    y = df["Date_Occurrences"]

    return X, y, df


def create_pipeline():
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), NUMERIC_COLUMNS),
            ("cat", OneHotEncoder(sparse_output=False), CATEGORICAL_COLUMNS),
        ]
    )

    pipeline = Pipeline(
        [
            ("preprocessor", preprocessor),
            (
                "gb",
                GradientBoostingRegressor(
                    learning_rate=0.05,
                    max_depth=4,
                    min_samples_leaf=2,
                    min_samples_split=10,
                    n_estimators=150,
                    random_state=42,
                    subsample=0.85,
                ),
            ),
        ]
    )
    return pipeline


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse:.2f}")
    print(f"Mean Absolute Error: {mae:.2f}")
    print(f"R^2 Score: {r2:.2f}")

    plt.figure(figsize=(12, 8))
    plt.scatter(y_test, y_pred, alpha=0.7)
    plt.title("Actual vs Predicted Values", fontsize=16)
    plt.xlabel("Actual", fontsize=14)
    plt.ylabel("Predicted", fontsize=14)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--")
    plt.tight_layout()
    plt.savefig("plots/actual_vs_predicted_values.png")
    # plt.show()

    residuals = y_test - y_pred
    plt.figure(figsize=(12, 8))
    sns.histplot(residuals, kde=True, bins=30)
    plt.title("Distribution of Residuals", fontsize=16)
    plt.xlabel("Residuals", fontsize=14)
    plt.ylabel("Count", fontsize=14)
    plt.tight_layout()
    plt.savefig("plots/distribution_of_residuals.png")
    # plt.show()

    feature_importances = model.named_steps["gb"].feature_importances_
    feature_names = NUMERIC_COLUMNS + list(
        model.named_steps["preprocessor"]
        .transformers_[1][1]
        .get_feature_names_out(CATEGORICAL_COLUMNS)
    )
    importance_df = pd.DataFrame(
        {"Feature": feature_names, "Importance": feature_importances}
    )
    importance_df = importance_df.sort_values(by="Importance", ascending=False)

    plt.figure(figsize=(14, 10))
    sns.barplot(x="Importance", y="Feature", data=importance_df)
    plt.title("Feature Importances", fontsize=16)
    plt.xlabel("Importance", fontsize=14)
    plt.ylabel("Feature", fontsize=14)
    plt.tight_layout()
    plt.savefig("plots/feature_importance.png")
    # plt.show()


def plot_data_overview(df):
    df[NUMERIC_COLUMNS].hist(bins=30, figsize=(18, 12))
    plt.suptitle("Feature Distributions", fontsize=18)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig("plots/feature_distributions.png")
    # plt.show()

    plt.figure(figsize=(14, 12))
    sns.heatmap(
        df[NUMERIC_COLUMNS + ["Date_Occurrences"]].corr(),
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
    )
    plt.title("Correlation Heatmap", fontsize=16)
    plt.tight_layout()
    plt.savefig("plots/correlation_heatmap.png")
    # plt.show()

    plt.figure(figsize=(12, 8))
    sns.histplot(df["Date_Occurrences"], kde=True, bins=30)
    plt.title("Target Variable Distribution (Date_Occurrences)", fontsize=16)
    plt.xlabel("Date Occurrences", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.tight_layout()
    plt.savefig("plots/target_variable_distribution.png")
    # plt.show()


def main():
    df = load_data()
    X, y, full_df = preprocess_data(df)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    pipeline = create_pipeline()
    pipeline.fit(X_train, y_train)

    os.makedirs("./model", exist_ok=True)
    joblib.dump(pipeline, "./model/gb_model.pkl")

    plot_data_overview(full_df)
    evaluate_model(pipeline, X_test, y_test)


if __name__ == "__main__":
    main()
