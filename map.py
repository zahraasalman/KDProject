import folium as f
from streamlit_folium import folium_static

m = f.Map(location=[45.5236, -122.6750])

folium_static(m)
