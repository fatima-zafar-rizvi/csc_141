# Original Loop Example:

'''
for eq_dict in all_eq_dicts:
    magnitude = eq_dict['properties']['mag']
    longitude = eq_dict['geometry']['coordinates'][0]
    latitude = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']

    magnitudes.append(magnitude)
    longitudes.append(longitude)
    latitudes.append(latitude)
    titles.append(title)
'''

# Refractores Loop

from pathlib import Path
import json

# Read data as a string and convert to a Python object.
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

magnitudes, longitudes, latitudes, titles = [], [], [], []

for eq_dict in all_eq_dicts:
    magnitudes.append(eq_dict['properties']['mag'])
    longitudes.append(eq_dict['geometry']['coordinates'][0])
    latitudes.append(eq_dict['geometry']['coordinates'][1])
    titles.append(eq_dict['properties']['title'])