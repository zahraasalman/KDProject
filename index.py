import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import folium_static

import map
import queries as Q


############################### FUNCTIONS ######################################
def _max_width_():  # CSS to make screen in wide mode
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

def find_index(search_item, list):
    i = 0
    while i < len(list):
        if search_item == list[i]:
            return i
        i += 1
    return "Not found"


def options():
    return_list = {}  # dictionary
    continent = 'all'
    region = 'all'
    country = 'all'

    if st.checkbox("Filter by Continent"):
        continents = {'continent': [], 'label': []}
        for cont in Q.get_continents():
            continents['continent'].append(cont[0])
            continents['label'].append(cont[1])
        option_continent = st.selectbox(
            'Which continents?',
            continents['label'])

        if option_continent:
            return_list['continent'] = option_continent
            index = find_index(option_continent, continents['label'])
            continent = continents['continent'][index]
        else:
            "No results found, please select a continent or unselect the checkbox!"

    if st.checkbox("Filter by Region"):
        regions = {'region': [], 'label': []}
        for reg in Q.get_regions(continent):
            regions['region'].append(reg[0])
            regions['label'].append(reg[1])
        option_region = st.selectbox(
            'Which Region?',
            regions['label'])

        if option_region:
            return_list['region'] = option_region
            index = find_index(option_region, regions['label'])
            region = regions['region'][index]
        else:
            "No results found, please select a region or unselect the checkbox!"

    countries = {'country': [], 'label': []}
    for count in Q.get_countries(continent, region):
        countries['country'].append(count[0])
        countries['label'].append(count[1])
    option_country = st.selectbox(
        'Which country?',
        countries['label'])
    return_list["country"] = option_country
    index = find_index(option_country, countries['label'])
    country = countries['country'][index]

    if st.checkbox("Select Capital"):
        capitals = {'capital': [], 'label': []}
        for cap in Q.get_capitals(country):
            capitals['capital'].append(cap[0])
            capitals['label'].append(cap[1])
        option_capital = st.selectbox(
            'Which capital?',
            capitals['label'])
        if option_capital:
            return_list["capital"] = option_capital
        else:
            "No results found, please select a capital or unselect the checkbox!"

    return return_list


############################### INTRODUCTION ####################################
_max_width_()
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

with col2:
    folium_static(map.m)

if st.button('Find Places'):
    "I want to die"
