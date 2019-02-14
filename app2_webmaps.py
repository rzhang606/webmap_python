import folium
import pandas as pd

#functions
def color_logic(elevation):
	''' Color logic for volcano markers: parameter-elevation'''
	if elevation < 1000:
		return 'green'
	elif 1000 <= elevation < 3000:
		return 'orange'
	else:
		return 'red'


#location is longitude, latitude, which is put into 'map' object
#zoom is optional parameter
map = folium.Map()

data = pd.read_csv("Volcanoes.txt")

latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])

#adds children objects for markers
#option1, add directly
#map.add_child(folium.Marker(location=[80,-100], popup="Hi I am a marker", icon=folium.Icon(color='green')))

#use a feature group to add children, RECOMMENDED (layer control)
fgv = folium.FeatureGroup(name="Volcanoes")

#zip() takes iterables and makes iterator that returns tuples of the iterables passed
for lat, longi, el in zip(latitude, longitude, elevation) :
	fgv.add_child(folium.CircleMarker(location=[lat, longi], popup="Elevation: %s m" % el,
	fill_color=color_logic(el), color='grey', fill_opacity=0.7))

#geojson data for polygon layer
#read() at the end to is to convert to string as GeoJson takes a string parameter now
#style function can be used to determine color, as shown with lambda function
#x['properties']['POP2005'] is saying x(the feature) determined by the population in the properties attribute key (JSON)
fg = folium.FeatureGroup(name='Population')

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange'
if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

#adds the feature group, which ontains all the individual children
map.add_child(fgv) #volcano points layer
map.add_child(fg) #population polygon layer

#toggle which layers to see
#should be after all the other children are added
map.add_child(folium.LayerControl())

#use folium to create html based off of the object
map.save("Map1.html")