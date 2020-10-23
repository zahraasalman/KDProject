import folium as f
from streamlit_folium import folium_static


def getMap(coordinates):  ### touples array! [(float, float), (float, float)]
    if not coordinates:  ## if no coordinates, show general map
        return folium_static(f.Map())

    mapIt = f.Map()
    for coord in coordinates:
        mapIt = f.Map(location=[coord[0], coord[1]], zoom_start=4)
        f.Marker([coord[0], coord[1]]).add_to(mapIt)

    return folium_static(mapIt)
