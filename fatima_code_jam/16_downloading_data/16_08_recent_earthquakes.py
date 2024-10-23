from pathlib import Path
import json
import matplotlib.pyplot as plt

# Read data as a string and convert to a Python object
path = Path('eq_data/m2.5_1_day.geojson') 
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

# Prepare lists for visualization
magnitudes, longitudes, latitudes = [], [], []

for eq_dict in all_eq_dicts:
    magnitudes.append(eq_dict['properties']['mag'])
    longitudes.append(eq_dict['geometry']['coordinates'][0])
    latitudes.append(eq_dict['geometry']['coordinates'][1])

# Create a scatter plot of the earthquakes
plt.figure(figsize=(10, 6))
plt.scatter(longitudes, latitudes, c=magnitudes, cmap='viridis', alpha=0.7, 
            edgecolors='k')
plt.colorbar(label='Magnitude')
plt.title('Recent Earthquakes in the Last Day')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()