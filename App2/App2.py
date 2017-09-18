
import folium
import pandas as pd

import json

def getColour(elev):
    return('#%02x%02x%02x' % (50, 100, int(elev/20)))

def getPopColor(pop):
    if pop < 1000000:
        return("grey")
    elif pop < 10000000:
        return("green")
    elif pop < 20000000:
        return("yellow")
    else:
        return("red")

volcanoes = pd.read_csv("./App2/Volcanoes_USA.txt")

map = folium.Map(location = [38,-100], zoom_start=6, tiles='Mapbox Bright')

fg = folium.FeatureGroup(name="Markers")

for index, row in volcanoes.iterrows():
    fg.add_child(folium.CircleMarker(location =[row["LAT"], row["LON"]], popup=str(row["ELEV"]) + " m",
                               color=getColour(row["ELEV"]),fill=True , radius=10))


fg2 = folium.FeatureGroup(name='Polygons')

fg2.add_child(folium.GeoJson(data=open("./App2/world.json", "r", encoding='utf-8-sig').read(),
                           style_function= lambda x: {'fillColor': getPopColor(int(x['properties']['POP2005'])),
                                                      'popup': x['properties']['POP2005']
                                                      } ,
                             highlight_function = lambda x: {'fillColor': "blue",
                                                              'popup': x['properties']['POP2005']
                                                              }))
map.add_child(fg)
map.add_child(fg2)

map.add_child(folium.LayerControl())

map.save("map1.html")
