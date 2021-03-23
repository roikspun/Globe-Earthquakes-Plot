import json
import plotly.graph_objects as go
from plotly.subplots import make_subplots

"""A visualization of 1.0+ magnitude"""
filename = '1+_earthquakes_past_30_days.geojson'
with open(filename, encoding='utf8') as f:
    rawdata_quakes = json.load(f)

data_quakes = rawdata_quakes['features']
graph_title = rawdata_quakes['metadata']['title']  # Optional Automatic Title for Each File

# List variables to store the data
mags, longs, lats, tag_location = [], [], [], []
tsu_lons, tsu_lats, tsu_tags = [], [], []
for event in data_quakes:
    mags.append(event['properties']['mag'])
    longs.append(event['geometry']['coordinates'][0])
    lats.append(event['geometry']['coordinates'][1])
    tag_location.append(event['properties']['title'])
# Checks for large oceanic events, that may indicate the event of a tsunami
    if event['properties']['tsunami'] == 1:  # Flag 1 if detected, 0 otherwise
        tsu_lons.append(event['geometry']['coordinates'][0])
        tsu_lats.append(event['geometry']['coordinates'][1])
        tsu_tags.append(event['properties']['title'])

# Creates the figure element
fig = make_subplots()
fig.add_trace(go.Scattergeo(
    lon=longs,  # longitude of the earthquake
    lat=lats,  # latitude of the earthquake
    hovertemplate=[f"{tag}<extra></extra>" for tag in tag_location],
    showlegend=False,
    marker=dict(
        size=[3.5*mag for mag in mags],  # This will make the markers easier to spot and see
        color=mags,  # adding another dimension of information with a color scale
        colorscale='Inferno',
        reversescale=True,  # The darker the color the higher the magnitude
        colorbar=dict(title='Magnitude')  # Color bar description
    ),
))
fig.update_geos(
    projection_type='orthographic',  # Creates a visualization of the earth as a globe
    lataxis_showgrid=True,
    lonaxis_showgrid=True,
    )
fig.update_layout(
    geo=dict(
        showlakes=True,
        lakecolor="rgb(153, 217, 234)",
        showcountries=True,
        landcolor="rgb(223, 223, 223)",
        showocean=True,
        oceancolor="rgb(215, 240, 247)",
    ),
    title=graph_title+" Retrieved on: March 19th, 2021 4:11pm GMT-6",
)
fig.add_trace(go.Scattergeo(  # Plot of probable tsunami events
    mode='text',
    lon=tsu_lons,
    lat=tsu_lats,
    hovertemplate=[f"{tag}<extra></extra>" for tag in tsu_tags],
    text='🌊',
    showlegend=False,  # This will avoid displaying the legends of each trace
    textfont=dict(
        size=20,
    )
))
fig.show()
