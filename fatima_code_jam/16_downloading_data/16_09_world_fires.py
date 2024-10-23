import pandas as pd
import plotly.express as px

# Load the data
fires_data = pd.read_csv('eq_data/world_fires_1_day.csv')

# Clean the data
fires_data = fires_data.dropna(subset=['latitude', 'longitude', 'brightness'])

# Create the map
fig = px.scatter_geo(fires_data,
                     lat='latitude',
                     lon='longitude',
                     color='brightness',
                     color_continuous_scale='Reds',
                     title='Global Fire Locations',
                     hover_name='brightness',
                     projection='natural earth')

fig.update_geos(showcoastlines=True, coastlinecolor="Black",
                showland=True, landcolor="lightgreen", showlakes=True, 
                lakecolor="aqua")
fig.show()