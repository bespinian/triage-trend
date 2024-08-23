import pandas as pd
import ephem
from datetime import datetime

# Define the start and end dates
start_date = datetime(2019, 1, 1)
end_date = datetime(2023, 12, 31)

# Create a list of dates between the start and end dates
date_range = pd.date_range(start_date, end_date)

# Initialize lists to store the data
dates = []
moon_phases = []

# Loop through each date and calculate the moon phase
for single_date in date_range:
    # Create an observer at a location in Switzerland (Bern)
    observer = ephem.Observer()
    observer.lat, observer.lon = '46.948', '7.4474'  # Bern, Switzerland
    observer.date = single_date

    # Calculate the moon phase
    moon = ephem.Moon(observer)
    phase = moon.phase  # Moon phase as a percentage

    dates.append(single_date)
    moon_phases.append(phase)

# Create a DataFrame with the results
moon_calendar_df = pd.DataFrame({
    'Date': dates,
    'Moon Phase (%)': moon_phases
})

# Save the DataFrame to a CSV file
moon_calendar_df.to_csv('moon_calendar_switzerland_2019_2023.csv', index=False)
