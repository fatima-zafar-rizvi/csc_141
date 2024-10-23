from pathlib import Path
import csv
import matplotlib.pyplot as plt

# Load the Sitka weather data
sitka_data = Path('weather_data/sitka_weather_2021_full.csv')
lines_sd = sitka_data.read_text().splitlines()

# Load the Death Valley weather data
death_valley_data = Path('weather_data/death_valley_2021_full.csv')
lines_dv = death_valley_data.read_text().splitlines()

# Initialize lists to store dates, tmax, and tmin values
dates_sd = []
tmax_sd = []
tmin_sd = []

dates_dv = []
tmax_dv = []
tmin_dv = []

# Read the CSV data for Sitka
reader_sd = csv.reader(lines_sd)
header_row_sd = next(reader_sd)

for index, row in enumerate(reader_sd):
    if 0 <= index <= 30:  
        dates_sd.append(row[2])
        tmax_value = row[7]
        tmin_value = row[8]
        if tmax_value:  # Check if the value is not empty
            tmax_sd.append(float(tmax_value))
        if tmin_value:  # Check if the value is not empty
            tmin_sd.append(float(tmin_value))

# Read the CSV data for Death Valley
reader_dv = csv.reader(lines_dv)
header_row_dv = next(reader_dv)

for index, row in enumerate(reader_dv):
    if 0 <= index <= 30:  
        dates_dv.append(row[2])
        tmax_value = row[6]
        tmin_value = row[7]
        if tmax_value:  # Check if the value is not empty
            tmax_dv.append(float(tmax_value))
        if tmin_value:  # Check if the value is not empty
            tmin_dv.append(float(tmin_value))

# Plotting temperatures
plt.figure(figsize=(12, 6))

# Sitka Temperature
plt.subplot(1, 2, 1)
plt.plot(dates_sd, tmin_sd, label='Sitka Min Temp', color='blue')
plt.plot(dates_sd, tmax_sd, label='Sitka Max Temp', color='lightblue')
plt.title('Sitka Temperature (2021)')
plt.xlabel('Date')
plt.ylabel('Temperature (°F)')
plt.ylim(0, 100)  # Adjust y-axis to same scale
plt.xticks(rotation=45)
plt.legend()

# Death Valley Temperature
plt.subplot(1, 2, 2)
plt.plot(dates_dv, tmin_dv, label='Death Valley Min Temp', color='orange')
plt.plot(dates_dv, tmax_dv, label='Death Valley Max Temp', color='yellow')
plt.title('Death Valley Temperature (2021)')
plt.xlabel('Date')
plt.ylim(0, 100)  # Adjust y-axis to same scale
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()