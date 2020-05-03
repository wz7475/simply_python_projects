from geopy.geocoders import ArcGIS
nom = ArcGIS()
import webbrowser
import folium

file1 = open("web_map\\data\\places.txt", "r", encoding="utf-8")
places=file1.readlines()
file1.close()  

html = """
<a href="https://www.google.com/search?q=%s" target="_blank">%s</a>
"""


fg = folium.FeatureGroup(name="My places")
map = folium.Map(location=[52, 21],
                 zoom_start=10)

coordinates=[]
file2 = open("web_map\\data\\coordinates.txt", "r+")
for i in range(len(places)):
    coordinates.append(nom.geocode(places[i]))
    file2.write(str(coordinates[i].latitude) +","+ str(coordinates[i].longitude)+"\n")
    iframe = folium.IFrame(html=html % (
        places[i], places[i]), width=75, height=35)
    fg.add_child(folium.Marker(location=[coordinates[i].latitude, coordinates[i].longitude],
                 zoom_start=4, color="red", popup=folium.Popup(
        iframe)))
file2.close()

map.add_child(fg)
map.save("web_map\\html\\moje_miejsca.html")
webbrowser.open("web_map\\html\\moje_miejsca.html")