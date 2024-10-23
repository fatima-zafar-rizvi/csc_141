from pathlib import Path
import csv
import matplotlib.pyplot as plt
import pandas as pd

# Load the Sitka weather data
sitka_data = Path('weather_data/sitka_weather_2021_full.csv')
lines = sitka_data.read_text().splitlines()

# Initialize lists to store dates and precipitation values
dates = []
prcp = []


# Read the CSV data
reader = csv.reader(lines)  
header_row = next(reader)

# Skip the first row (header) and read only rows 2 to 31 (indices 1 to 30)
for index, row in enumerate(reader):
    if 1 <= index <= 30:  # Only process rows 2 to 31
        dates.append(row[2])
        prcp_value = row[5]
        if prcp_value:  # Check if the value is not empty
            prcp.append(float(prcp_value))

# Plotting daily rainfall
plt.figure(figsize=(12, 6))
plt.plot(dates, prcp, color='blue', marker='o', linestyle='-', markersize=3)
plt.title('Daily Rainfall in Sitka (2021)')
plt.xlabel('Date')
plt.ylabel('Daily Rainfall (inches)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()