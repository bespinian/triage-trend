from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
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

    return X, y, df['Weekday']

def create_pipeline():
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_columns),
            ('cat', OneHotEncoder(), categorical_columns)
        ]
    )

    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('ridge', Ridge())
    ])
    return pipeline

def train_model(pipeline, X_train, y_train):
    param_grid = {
        'ridge__alpha': [0.1, 1.0, 10.0],  # Regularization strength
    }

    grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='neg_mean_squared_error')
    grid_search.fit(X_train, y_train)

    return grid_search.best_estimator_

def evaluate_model(pipeline, X_test, y_test, weekdays_test):
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

    # Residual analysis
    residuals = y_test - y_pred
    print("\nResiduals (Actual - Predicted):")
    print(residuals.describe())

    plt.figure(figsize=(10, 6))
    sns.histplot(residuals, kde=True)
    plt.title('Distribution of Residuals')
    plt.xlabel('Residuals')
    plt.show()

    # Plot actual vs predicted
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.7)
    plt.title('Actual vs Predicted Values')
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # Diagonal line
    plt.show()

    # Feature importances (for Ridge or similar models)
    if hasattr(pipeline.named_steps['ridge'], 'coef_'):
        coef = pipeline.named_steps['ridge'].coef_
        print("\nFeature Coefficients:")
        for feature, importance in zip(numeric_columns + ['IsWeekend'], coef):
            print(f"{feature}: {importance:.4f}")

    # Analyze predictions by weekday
    weekday_preds = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred, 'Weekday': weekdays_test})
    weekday_analysis = weekday_preds.groupby('Weekday').agg(['mean', 'std'])
    print("\nPrediction Analysis by Weekday:")
    print(weekday_analysis)

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Weekday', y='Predicted', data=weekday_preds)
    plt.title('Boxplot of Predictions by Weekday')
    plt.show()

def main():
    df = load_data()
    X, y, weekdays = preprocess_data(df)
    X_train, X_test, y_train, y_test, weekdays_train, weekdays_test = train_test_split(X, y, weekdays, test_size=0.3, random_state=42)
    pipeline = create_pipeline()
    best_pipeline = train_model(pipeline, X_train, y_train)
    evaluate_model(best_pipeline, X_test, y_test, weekdays_test)
