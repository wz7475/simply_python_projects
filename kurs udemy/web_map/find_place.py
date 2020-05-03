import webbrowser
import folium
from geopy.geocoders import ArcGIS
nom = ArcGIS()
with open("web_map\\data\\find.txt") as f:
    address = f.read()
m=nom.geocode(address)
map = folium.Map(location=[m.latitude, m.longitude], zoom_start=8)
folium.Marker(location=[m.latitude, m.longitude], color="green").add_to(map)
map.save("web_map\\html\\find_place.html")
webbrowser.open("web_map\\html\\find_place.html")
