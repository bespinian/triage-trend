import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from triage_trend.load_data import load_data

def preprocess_data(df):
    # Fill missing values for Weekday
    if df['Weekday'].isnull().any():
        df['Weekday'] = df['Weekday'].fillna(df['Weekday'].mode()[0])
    
    # Apply other preprocessing steps if needed, but do not one-hot encode 'Weekday'
    
    return df

def data_analysis(df):
    # Descriptive Statistics
    print("Descriptive Statistics:\n", df.describe())
    print("\nFrequency of Categorical Data (if any):\n", df.select_dtypes(include=['category', 'object']).apply(pd.Series.value_counts))

    # Missing Values Analysis
    print("\nMissing Values:\n", df.isnull().sum())

    # Visualization: Distribution of 'Date_Occurrences'
    plt.figure(figsize=(12, 6))
    sns.histplot(df['Date_Occurrences'], kde=True)
    plt.title('Distribution of Date Occurrences')
    plt.xlabel('Occurrences')
    plt.ylabel('Frequency')
    plt.show()

    # Correlation Heatmap (excluding non-numeric columns)
    numeric_df = df.select_dtypes(include=[np.number])
    plt.figure(figsize=(12, 10))
    sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Feature Correlation Matrix (Numeric Features Only)')
    plt.show()

    # Boxplot: Occurrences per Weekday
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Weekday', y='Date_Occurrences', data=df)
    plt.title('Boxplot of Date Occurrences per Weekday')
    plt.xlabel('Weekday')
    plt.ylabel('Date Occurrences')
    plt.show()

def main():
    df = load_data()  # Load data from your specific function
    df_preprocessed = preprocess_data(df)  # Preprocess the data
    data_analysis(df_preprocessed)  # Perform analysis
