import webbrowser
import folium

file1 = open("web_map\\data\\coordinates.txt", "r")
coordinates=file1.readlines()
file1.close()  

file2 = open("web_map\\data\\places.txt", "r", encoding="utf-8")
places=file2.readlines()
file2.close()  

html = """
<a href="https://www.google.com/search?q=%s" target="_blank">%s</a>
"""

fg = folium.FeatureGroup(name="My places")
map = folium.Map(location=[52, 21], zoom_start=8)


for pl, cor in zip(places, coordinates):
    wsp=cor.split(",")
    iframe = folium.IFrame(html=html % (pl, pl), width=75, height=35)
    fg.add_child(folium.Marker(location=[wsp[0], wsp[1]],
                 zoom_start=4, color="red", popup=folium.Popup(
        iframe)))

map.add_child(fg)
map.save("web_map\\html\\moje_miejsca_offline.html")
webbrowser.open("web_map\\html\\moje_miejsca_offline.html")