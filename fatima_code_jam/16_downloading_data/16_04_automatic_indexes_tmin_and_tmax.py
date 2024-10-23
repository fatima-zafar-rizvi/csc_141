
from pathlib import Path
import csv
import matplotlib.pyplot as plt

# Load the weather data
weather_data = Path('weather_data/sitka_weather_2021_full.csv')  
lines = weather_data.read_text().splitlines()

# Initialize lists to store dates, tmax, and tmin values
dates = []
tmax = []
tmin = []

# Read the CSV data
reader = csv.reader(lines)
header_row = next(reader)

# Determine the indexes for TMIN and TMAX
tmin_index = header_row.index('TMIN')
tmax_index = header_row.index('TMAX')

# Extract and format the station name
station_name = weather_data.stem.replace('_', ' ').title()


# Read data and populate the lists
for index, row in enumerate(reader):
    if 0 <= index <= 30:  
        dates.append(row[2])
        tmax_value = row[tmax_index]
        tmin_value = row[tmin_index]
        if tmax_value:  # Check if the value is not empty
            tmax.append(float(tmax_value))
        if tmin_value:  # Check if the value is not empty
            tmin.append(float(tmin_value))

# Plotting temperatures for the selected station
plt.figure(figsize=(12, 6))
plt.plot(dates, tmin, label=f'{station_name} Min Temp', color='pink')
plt.plot(dates, tmax, label=f'{station_name} Max Temp', color='red')

# Set the title using the station name
plt.title(f'{station_name} Temperature (2021)')
plt.xlabel('Date')
plt.ylabel('Temperature (°F)')
plt.ylim(0, 100)  # Use the same scale for comparison
plt.xticks(rotation=45)
plt.legend()
plt.show()
