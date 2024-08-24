from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, StackingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Load your data here
from triage_trend.load_data import load_data

def preprocess_data(df):
    df['Weekday'] = df['Weekday'].map({
        'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
        'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6
    })

    # Handle datetime columns
    for col in df.columns:
        if np.issubdtype(df[col].dtype, np.datetime64):
            df[f'{col}_ordinal'] = pd.to_datetime(df[col]).map(pd.Timestamp.toordinal)
            df = df.drop(columns=[col])

    # Ensure all features are numeric
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype('category').cat.codes

    # Fill missing values
    df = df.fillna(df.mean())

    # Add IsWeekend feature
    df['IsWeekend'] = df['Weekday'].isin([5, 6]).astype(int)

    X = df.drop(columns=['Date_Occurrences'])
    y = df['Date_Occurrences']

    return X, y

def evaluate_model(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'{model_name}: MSE = {mse:.2f}, MAE = {mae:.2f}, R^2 = {r2:.2f}')

    # Plot actual vs predicted
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.6)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.title(f'Actual vs Predicted Values ({model_name})')
    plt.show()

    # Plot residuals
    residuals = y_test - y_pred
    plt.figure(figsize=(8, 6))
    sns.histplot(residuals, kde=True, bins=30)
    plt.title(f'Distribution of Residuals ({model_name})')
    plt.xlabel('Residuals')
    plt.ylabel('Count')
    plt.show()

def main():
    df = load_data()
    X, y = preprocess_data(df)

    # Ensure all data types in X are numeric
    if not np.all([np.issubdtype(dtype, np.number) for dtype in X.dtypes]):
        raise ValueError("All features must be numeric. Check data preprocessing.")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    models = {
        'Polynomial Regression': Pipeline([
            ('poly', PolynomialFeatures(degree=2)),
            ('scaler', StandardScaler()),
            ('regressor', LinearRegression())
        ]),
        'Random Forest': RandomizedSearchCV(
            RandomForestRegressor(random_state=42),
            param_distributions={
                'n_estimators': [100, 200, 300],
                'max_depth': [None, 10, 20, 30],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 2, 4]
            },
            n_iter=50, cv=3, n_jobs=-1, random_state=42
        ),
        'Gradient Boosting': RandomizedSearchCV(
            GradientBoostingRegressor(random_state=42),
            param_distributions={
                'n_estimators': [100, 200, 300],
                'learning_rate': [0.01, 0.1, 0.2],
                'max_depth': [3, 5, 7],
                'subsample': [0.8, 1.0]
            },
            n_iter=50, cv=3, n_jobs=-1, random_state=42
        ),
        'Neural Network': Pipeline([
            ('scaler', StandardScaler()),
            ('regressor', MLPRegressor(
                random_state=42, max_iter=1500, hidden_layer_sizes=(100, 50), learning_rate_init=0.01))
        ]),
        'Ensemble Stacking': StackingRegressor(
            estimators=[
                ('rf', RandomForestRegressor(random_state=42)),
                ('gb', GradientBoostingRegressor(random_state=42))
            ],
            final_estimator=LinearRegression()
        )
    }

    for model_name, model in models.items():
        model.fit(X_train, y_train)
        evaluate_model(model, X_test, y_test, model_name)

if __name__ == "__main__":
    main()
