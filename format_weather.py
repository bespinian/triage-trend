import pandas as pd
import numpy as np

# Function to calculate cloudiness based on Global Radiation (StrGlo)
def calculate_cloudiness(global_radiation):
    max_possible_radiation = 1000  # A rough estimate of max possible radiation
    return np.clip(1 - (global_radiation / max_possible_radiation), 0, 1)  # Ensure value is between 0 and 1

# Read the CSV data
df = pd.read_csv('data/weather_data_2023.csv')

# Parse the datetime column to pandas datetime type
df['Datum'] = pd.to_datetime(df['Datum'])

# Group data by date and location to calculate location-specific daily metrics
grouped = df.groupby(['Datum', 'Standort'], as_index=False)

# Define a function to calculate daily features per location
def calculate_daily_features(group):
    features = {}
    features['Average_Temperature'] = group.loc[group['Parameter'] == 'T', 'Wert'].mean()
    features['Max_Temperature'] = group.loc[group['Parameter'] == 'T_max_h1', 'Wert'].max()
    features['Total_Rain_Duration'] = group.loc[group['Parameter'] == 'RainDur', 'Wert'].sum()
    features['Average_Pressure'] = group.loc[group['Parameter'] == 'p', 'Wert'].mean()
    features['Average_Global_Radiation'] = group.loc[group['Parameter'] == 'StrGlo', 'Wert'].mean()

    # Recalculate cloudiness
    if pd.notnull(features['Average_Global_Radiation']):
        features['Cloudiness'] = calculate_cloudiness(features['Average_Global_Radiation'])
    else:
        features['Cloudiness'] = np.nan

    return pd.Series(features)

# Apply the feature calculation function to each group
daily_features = grouped.apply(calculate_daily_features).reset_index(drop=True)

# Clean up unrealistic values
# Total_Rain_Duration: Clip values to be within realistic limits
daily_features['Total_Rain_Duration'] = np.clip(daily_features['Total_Rain_Duration'], 0, 1440)

# Fill missing values with reasonable estimates
daily_features['Cloudiness'] = daily_features['Cloudiness'].fillna(0.5)  # Assuming neutral cloudiness if data is missing

# Filter only numeric columns before aggregating across locations
numeric_columns = daily_features.select_dtypes(include=[np.number]).columns
final_features = daily_features.groupby('Datum')[numeric_columns].mean().reset_index()

# Display the result
print(final_features)

# Save to a new CSV file
final_features.to_csv('data/cleaned_weather_features_2023.csv', index=False)
