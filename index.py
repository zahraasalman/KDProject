import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import folium_static

import folium as f
from streamlit_folium import folium_static

import map
import queries as Q


############################### FUNCTIONS ######################################
def max_width():  # CSS to make screen in wide mode
    max_width_str = f"max-width: 2000px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )


def options():
    return_list = {} #dictionary
    continent = 'all'
    region = 'all'
    country = 'all'

    if st.checkbox("Filter by Continent"):
        option_continent = st.selectbox(
            'Which continents?',
            Q.get_continents())

        if option_continent:
            return_list['continent'] = option_continent
            continent = option_continent
        else:
            "No results found, please select a continent or unselect the checkbox!"

    if st.checkbox("Filter by Region"):
        option_region = st.selectbox(
            'Which Region?',
            Q.get_regions(continent))

        if option_region:
            return_list['continent'] = option_region
            region = option_region
        else:
            "No results found, please select a region or unselect the checkbox!"

    option_country = st.selectbox(
        'Which country?',
        Q.get_countries(continent, region))
    return_list["country"] = option_country
    country = option_country
    options.country = country
    if st.checkbox("Select Capital"):
        option_capital = st.selectbox(
            'Which capital?',
            Q.get_capitals(country))
        if option_capital:
            return_list["capital"] = option_capital
        else:
            "No results found, please select a capital or unselect the checkbox!"

    return return_list


############################### INTRODUCTION ####################################
max_width()
st.title("Welcome to <app name>")
"""
This app is made to help you get your information before you travel to your touisty destination blah blah idc. \n
This is multi-line and it's awesome
"""
st.subheader("Please select the country or capital that you want to view")
"""

"""
col1, col2 = st.beta_columns([2, 3])

with col1:
    results_from_funoptions = options()
    for key, value in results_from_funoptions.items():
        "You selected " + key + ": " + value

# I have decided to place the col2 in the button fucntion, the map will now appear as the user gives input.
# Abandoned map.py as this required input from index.py which would cause an import circle and crash the program.

if st.button('Find Places'):
    cords = Q.get_country_coordinates(options.country)[1]
    print(cords)
    # print(Q.get_country_coordinates(options.country))
    map2 = f.Map(location=[cords[0], cords[1]])

    with col2:
         folium_static(map2)