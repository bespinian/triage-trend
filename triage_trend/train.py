from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.compose import ColumnTransformer
from triage_trend.load_data import load_data

# Global definitions for column names
CATEGORICAL_COLUMNS = ['Weekday']
NUMERIC_COLUMNS = [
    'Average_Temperature', 'Max_Temperature', 'Total_Rain_Duration',
    'Average_Pressure', 'Average_Global_Radiation', 'Cloudiness',
    'Moon Phase (%)', 'IsVacationAargau', 'IsVacationZug',
    'IsVacationSchwyz', 'IsVacationSt_gallen', 'IsVacationSchaffhausen',
    'IsVacationThurgau'
]

def map_weekdays(df):
    """Map weekday names to numerical values."""
    weekday_mapping = {
        'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
        'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6
    }
    df['Weekday'] = df['Weekday'].map(weekday_mapping)
    return df

def handle_missing_values(df):
    """Fill missing values in both numeric and categorical columns."""
    numeric_cols = df.select_dtypes(include=['number']).columns.drop('Date_Occurrences')
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    for col in CATEGORICAL_COLUMNS:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df

def preprocess_data(df):
    """Preprocess the input DataFrame."""
    df = map_weekdays(df)
    df = handle_missing_values(df)

    # Add 'IsWeekend' feature
    df['IsWeekend'] = df['Weekday'].isin([5, 6]).astype(int)

    # Select only relevant columns for modeling
    df = df.select_dtypes(exclude=['datetime64'])
    X = df.drop(columns=['Date_Occurrences'])
    y = df['Date_Occurrences']

    return X, y

def create_pipeline():
    """Create a machine learning pipeline with preprocessing and Gradient Boosting."""
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), NUMERIC_COLUMNS),
            ('cat', OneHotEncoder(), CATEGORICAL_COLUMNS)
        ]
    )

    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('gb', GradientBoostingRegressor(
            learning_rate=0.05, max_depth=4, min_samples_leaf=2,
            min_samples_split=10, n_estimators=150, random_state=42,
            subsample=0.85
        ))
    ])
    return pipeline

def evaluate_model(model, X_test, y_test):
    """Evaluate the model and print performance metrics."""
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Mean Squared Error: {mse:.2f}')
    print(f'Mean Absolute Error: {mae:.2f}')
    print(f'R^2 Score: {r2:.2f}')

def main():
    df = load_data()
    X, y = preprocess_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    pipeline = create_pipeline()
    pipeline.fit(X_train, y_train)

    evaluate_model(pipeline, X_test, y_test)

if __name__ == "__main__":
    main()
