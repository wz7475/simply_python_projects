from geopy.geocoders import ArcGIS
nom = ArcGIS()
import webbrowser
import folium
import pandas

df1 = pandas.read_csv("web_map\\data\\Volcanoes.txt")
df2 = pandas.read_csv("web_map\\data\\cities.txt")

lon = list(df1["LON"])
lat = list(df1["LAT"])
elev = list(df1["ELEV"])
name = list(df1["NAME"])
type_v = list(df1["TYPE"])
cities = list(df2["MIASTO"])
countries = list(df2["COUNTRY"])

html1 = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%s+volcano" target="_blank">%s</a><br>
Height: %s m<br>
Type: %s
"""

html2 = """
<a href="https://www.google.com/search?q=%s+city" target="_blank">%s</a><br>
<a href="https://www.google.com/search?q=%s" target="_blank">%s</a>
"""

fg1 = folium.FeatureGroup(name="Vulcanoes")
map = folium.Map(location=[38, -120],
                 zoom_start=4, tiles="Stamen Terrain")
for lt, ln, el, name, tp in zip(lat, lon, elev, name, type_v):
    if(el < 1000): color = "green"
    elif(el < 3000): color = "orange"
    else: color = "red"
    iframe = folium.IFrame(html=html1 % (
        name, name, el, tp), width=200, height=100)
    fg1.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(
        iframe), fill_color=color, radius=8, color="grey", fill_opacity=0.7))

fg2 = folium.FeatureGroup(name="Population")
fg2.add_child(folium.GeoJson(open('web_map\\data\\world.json', 'r', encoding="utf-8-sig").read(),
           name='geojson',
           style_function=lambda x: {'fillColor': 'green' if
  x['properties']['POP2005'] < 10000000
       else 'orange' if 10000000 <= x['properties']['POP2005'] <= 20000000 else 'red'},
       ))

fg3 = folium.FeatureGroup(name="Cities")

for cit, coun in zip(cities, countries):
    m = nom.geocode(cit)
    iframe = folium.IFrame(html=html2 % (
        cit, cit, coun, coun), width=150, height=75)
    fg3.add_child(folium.Marker(location=[m.latitude, m.longitude],
                 zoom_start=8, color="green", popup=folium.Popup(
        iframe)))

map.add_child(fg2)
map.add_child(fg3)
map.add_child(fg1)

map.add_child(folium.LayerControl())
map.save("web_map\\html\\main_map.html")
webbrowser.open("web_map\\html\\main_map.html")
