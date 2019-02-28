#import folium
#hello2 = folium.Map()
#fghello = folium.FeatureGroup()
#for lat, lon in zip(lats, lons):
#      fghello.add_child(folium.CircleMarker(location = [lat,lon], fill = True))
#hello2.add_child(fghello)


import csv
with open('C:\\Users\\gasto\\Documents\\Python-Narrative-Journey-master\\Python-Narrative-Journey-master\\16-Violet-Mission-Mapping-with-Python\\countries.csv')as f:
    file = csv.reader(f)
    for row in file:
        print(row)
lats = []
longs = []
with open('C:\\Users\\gasto\\Documents\\Python-Narrative-Journey-master\\Python-Narrative-Journey-master\\16-Violet-Mission-Mapping-with-Python\\countries.csv')as f:
    file = csv.reader(f)
    for ab,lat,long,name in list(file)[1:]:
        lats.append(float(lat))
        longs.append(float(long))
