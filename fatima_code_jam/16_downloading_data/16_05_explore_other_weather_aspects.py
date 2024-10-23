from pathlib import Path
import csv
import matplotlib.pyplot as plt

# Load the Reading weather data
brooklyn_data = Path('weather_data/brooklyn_2023_december.csv')
lines = brooklyn_data.read_text().splitlines()

# Initialize lists to store dates and precipitation values
dates = []
prcp = []

# Read the CSV data
reader = csv.reader(lines)  
header_row = next(reader)

# Extract Data
for row in reader:
    dates.append(row[2])  
    prcp.append(float(row[3]))  

# Plotting Brooklyn rainfall in December 2023
plt.figure(figsize=(12, 6))
plt.plot(dates, prcp, color='purple', marker='o', linestyle='-', markersize=3)
plt.title('Daily Rainfall in Brooklyn, December 2023')
plt.xlabel('Date')
plt.ylabel('Daily Rainfall (inches)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()