import folium
import pandas


data  = pandas.read_csv("volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def elevition_color(elev):
    if elev > 3000:
        return "black"
    elif elev >2000 :
        return "darkred"
    elif elev > 1500:
        return "red"
    elif elev > 1000:
        return "orange"
    else:
        return "green"


map = folium.Map(location=[38.5,-99.09],zoom_start=6, tiles="Stamen Terrain")
fg_v= folium.FeatureGroup(name = "Volcanos")

for lt,ln,el,name in zip(lat,lon,elev,name):
    fg_v.add_child(folium.CircleMarker(location = [lt,ln] ,radius=6 ,fill=True,fill_opacity = 0.9,color="gray",popup = "the elevetion in {} volcano is: {} m".format(name,el),fill_color =  elevition_color(el)))

fg_p= folium.FeatureGroup(name = "Population")
fg_p.add_child(folium.GeoJson(data= open("world.json",'r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 1000000 
else 'orange' if 10000000<=x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fg_v)
map.add_child(fg_p)
map.add_child(folium.LayerControl())

map.save("map1.html")

