import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

def load_data(file_path):
    """Load the dataset from the CSV file."""
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    """Preprocess the data: handle categorical variables, date parsing, and missing values."""
    # Define the categorical columns
    categorical_columns = [
        'Fall_Land_Wohnort',
        'Fall_Kanton_wohnort',
        'Grenzkanton_ZH',
        'Psychiatrieregion ZH',
        'Fallerfassung_ZuweisungWochentag',
        'Fall_Eintritt_Tag',
        'Fuersorgische_Unterbringung_bei_Eintritt',
        'Eintritt'
    ]

    # Convert the date columns to datetime
    date_columns = [
        'Fallerfassung_Zuweisungsdatum',
        'Fall_Eintritt_Datum'
    ]

    # Drop time columns that are causing issues
    time_columns = [
        'Fallerfassung_Zuweisungsuhrzeit',
        'Fall_Eintritt_Uhrzeit'
    ]
    df = df.drop(columns=time_columns)

    for col in date_columns:
        df[col] = pd.to_datetime(df[col], format='%m/%d/%y', errors='coerce')  # Convert dates, coerce errors to NaT

    # Handle `NaT` values (e.g., fill with a placeholder or drop these rows)
    df[date_columns] = df[date_columns].fillna(pd.Timestamp("1970-01-01"))  # Example: fill NaT with a default date

    # Handle missing values
    # Fill numeric columns with their mean
    numeric_columns = df.select_dtypes(include=['number']).columns
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

    # Fill categorical columns with the most frequent value (mode)
    for col in categorical_columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Label encoding for categorical variables
    label_encoders = {col: LabelEncoder().fit(df[col]) for col in categorical_columns}
    for col, encoder in label_encoders.items():
        df[col] = encoder.transform(df[col])

    # Drop date columns if they are not needed for modeling
    df = df.drop(columns=date_columns)

    # Split data into features and target variable
    X = df.drop(columns=['Eintritt'])
    y = df['Eintritt']

    return X, y


def create_pipeline():
    """Create a pipeline with feature scaling and a Random Forest model."""
    pipeline = Pipeline([
        ('scaler', StandardScaler()),  # Feature scaling
        ('rf', RandomForestClassifier(n_estimators=100, random_state=42))  # Random Forest model
    ])
    return pipeline

def train_model(pipeline, X_train, y_train):
    """Train the pipeline model."""
    pipeline.fit(X_train, y_train)

def evaluate_model(pipeline, X_test, y_test):
    """Evaluate the model and print the accuracy."""
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.2f}')

def main():
    """Main function to run the entire pipeline."""
    file_path = 'data/clienia_dataset.csv'

    # Load the data
    df = load_data(file_path)

    # Preprocess the data
    X, y = preprocess_data(df)

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Create the pipeline
    pipeline = create_pipeline()

    # Train the model
    train_model(pipeline, X_train, y_train)

    # Evaluate the model
    evaluate_model(pipeline, X_test, y_test)
