import folium

#location is longitude, latitude, which is put into 'map' object
#zoom is optional parameter
map = folium.Map(location=[80,-100], zoom_start=6)


#adds children objects for markers
#option1, add directly
#map.add_child(folium.Marker(location=[80,-100], popup="Hi I am a marker", icon=folium.Icon(color='green')))

#use a feature group to add children, RECOMMENDED (layer control)
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[80,-100], popup="Hi I am a marker", icon=folium.Icon(color='green')))
map.add_child(fg)


#use folium to create html based off of the object
map.save("Map1.html")