import folium as f
from streamlit_folium import folium_static


def getMap(coordinates, zoom, cities_utilities = None):  ### touples array! [(float, float), (float, float)]
    if not coordinates:  ## if no coordinates, show general map
        return folium_static(f.Map())

    mapIt = f.Map()
    for coord in coordinates:
        mapIt = f.Map(location=[coord[0], coord[1]], zoom_start=zoom)
        f.Marker([coord[0], coord[1]]).add_to(mapIt)

    if cities_utilities is not None:
        for city in cities_utilities:
            print(city[1])
            if city[1] is not None:
                f.Marker([city[1][0][0], city[1][0][1]], popup="<b>Location:</b>" + city[0]).add_to(mapIt)
            else:
                pass

    return folium_static(mapIt)