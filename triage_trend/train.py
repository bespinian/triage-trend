from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt
import pandas as pd
from triage_trend.load_data import load_data

# Define global columns
categorical_columns = ['Weekday']
numeric_columns = [
    'Average_Temperature',
    'Max_Temperature',
    'Total_Rain_Duration',
    'Average_Pressure',
    'Average_Global_Radiation',
    'Cloudiness',
    'Moon Phase (%)',
    'IsVacationAargau',
    'IsVacationZug',
    'IsVacationSchwyz',
    'IsVacationSt_gallen',
    'IsVacationSchaffhausen',
    'IsVacationThurgau',
]

def preprocess_data(df):
    # Map weekdays to numerical values
    weekday_mapping = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
    }
    df['Weekday'] = df['Weekday'].map(weekday_mapping)

    # Handle missing values in numerical columns
    numeric_columns_local = df.select_dtypes(include=['number']).columns.drop('Date_Occurrences')
    numeric_columns_local = list(numeric_columns_local)
    df[numeric_columns_local] = df[numeric_columns_local].fillna(df[numeric_columns_local].mean())

    # Fill missing values in categorical columns
    for col in categorical_columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Add IsWeekend feature
    df['IsWeekend'] = df['Weekday'].isin([5, 6]).astype(int)

    numeric_columns_local.extend(['IsWeekend'])

    df = df.select_dtypes(exclude=['datetime64'])

    X = df.drop(columns=['Date_Occurrences'])
    y = df['Date_Occurrences']

    return X, y

def create_pipeline():
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_columns),
            ('cat', OneHotEncoder(), categorical_columns)
        ]
    )

    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('gbr', GradientBoostingRegressor(random_state=42))
    ])
    return pipeline

def train_model(pipeline, X_train, y_train):
    param_grid = {
        'gbr__n_estimators': [100, 200],
        'gbr__max_depth': [3, 5, 7],
        'gbr__learning_rate': [0.01, 0.1, 0.2],
        'gbr__subsample': [0.8, 1.0],
    }

    grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='neg_mean_squared_error')
    grid_search.fit(X_train, y_train)

    return grid_search.best_estimator_

def evaluate_model(pipeline, X_test, y_test):
    y_pred = pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Mean Squared Error: {mse:.2f}')
    print(f'Mean Absolute Error: {mae:.2f}')
    print(f'R^2 Score: {r2:.2f}')

    # Compare predicted and actual values
    comparison_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print("\nComparison of Actual vs Predicted:")
    print(comparison_df.head(20))  # Display the first 20 rows for review

    # Plot actual vs predicted
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.7)
    plt.title('Actual vs Predicted Values')
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # Diagonal line
    plt.show()

def main():
    df = load_data()
    X, y = preprocess_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    pipeline = create_pipeline()
    best_pipeline = train_model(pipeline, X_train, y_train)
    evaluate_model(best_pipeline, X_test, y_test)
