import folium as f
from streamlit_folium import folium_static
import streamlit as st


def getMap(coordinates, zoom):  ### touples array! [(float, float), (float, float)]
    if not coordinates:  ## if no coordinates, show general map
        pass
    else:
        mapIt = f.Map()
    for coord in coordinates:
        mapIt = f.Map(location=[coord[0], coord[1]], zoom_start=zoom)
        f.Marker([coord[0], coord[1]]).add_to(mapIt)

    return folium_static(mapIt)