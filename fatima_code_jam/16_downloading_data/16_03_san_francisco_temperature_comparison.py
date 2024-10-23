from pathlib import Path
import csv
import matplotlib.pyplot as plt

# Load the San Francisco weather data
san_francisco_data = Path('weather_data/san_francisco_2021_full.csv')
lines_sf = san_francisco_data.read_text().splitlines()

# Initialize lists to store dates, tmax, and tmin values
dates_sf = []
tmax_sf = []
tmin_sf = []

# Read the CSV data for San Francisco
reader_sf = csv.reader(lines_sf)
header_row_sf = next(reader_sf)

for index, row in enumerate(reader_sf):
    if 0 <= index <= 30:  
        dates_sf.append(row[2])
        tmax_value = row[6]
        tmin_value = row[7]
        if tmax_value:  # Check if the value is not empty
            tmax_sf.append(float(tmax_value))
        if tmin_value:  # Check if the value is not empty
            tmin_sf.append(float(tmin_value))


# Plotting temperatures for San Francisco
plt.figure(figsize=(12, 6))
plt.plot(dates_sf, tmin_sf, label='San Francisco Min Temp', color='green')
plt.plot(dates_sf, tmax_sf, label='San Francisco Max Temp', color='lightgreen')
plt.title('San Francisco Temperature (2021)')
plt.xlabel('Date')
plt.ylabel('Temperature (°F)')
plt.ylim(0, 100)  # Use the same scale for comparison
plt.xticks(rotation=45)
plt.legend()
plt.show()