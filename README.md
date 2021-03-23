# Globe-Earthquakes-Plot
Plotting of 1.0+ magnitude earthquakes and oceanic events (probable tsunamis) in a orthographic projection

This is a simple exercise of the use of (GEO)JSON and Plotly. It graphs all seismic events in a magnitude of 1 or higher around the world. Data was retrieved from the U.S. Geological Survey Website https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php on March, 19th 4:11 GMT-6. 

As well, I wanted to implement a quick and recognizable way to show large oceanic events, that may have caused a tsunami. For that reason I choose to use the water wave emoji as marker, using the 'text' mode in  Scattergeo to have a wide array of icons and symbols (UTF-8)

Future work will include the auto-update feature and other meteorological events, turned on/off using a toggle-button , such as tornados, hurricanes, wild fires, etc...

