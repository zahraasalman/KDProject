import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import folium_static

import map
import queries as Q


# ###################################### DATA ########################################
#
# df = pd.DataFrame({  # Data for options() that lets user pick the country/region/continent/capital
#     'Continents': Q.get_continents,
#     'Regions': ['Choose an option', 'Northwestern Europe', 'Middle East'],
#     'Countries': Q.get_countries(),
#     'Capitals': ['Choose an option', 'Amsterdam', 'Cairo']
# })


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


def options():  # lets user pick the country/region/continent/capital
    return_list = []
    continent = 'all'
    region = 'all'
    country = 'all'

    if st.checkbox("Filter by Continent"):
        option_continent = st.selectbox(
            'Which continents?',
            Q.get_continents())
        return_list.append(option_continent)
        continent = option_continent

    if st.checkbox("Filter by Region"):
        option_region = st.selectbox(
            'Which continents?',
            Q.get_regions(continent))
        return_list.append(option_region)
        region = option_region

    option_country = st.selectbox(
        'Which country?',
        Q.get_countries(continent, region))
    return_list.append(option_country)
    country = option_country
    if st.checkbox("Select Capital"):
        option_capital = st.selectbox(
            'Which capital?',
            Q.get_capitals(country))
        return_list.append(option_capital)

    return return_list


############################### INTRODUCTION ####################################
_max_width_()
st.title("Welcome to <app name>")
"""
This app is made to help you get your information before you travel to your touisty destination blah blah idc. \n
This is multi-line and it's awesome
"""
st.subheader("Please select the country or city you want to view")
"""

"""
col1, col2 = st.beta_columns([2, 3])

with col1:
    datatypes = ['Continent', 'Region', 'Country', 'Capital']
    results_from_funoptions = options()
    j = 0
    for i in results_from_funoptions:
        if i == 'Choose an option':  # to ignore if nothing's selected
            i = ''

        if type(i) is list:  # there's a multi-select
            for x in i:
                "You selected", datatypes[j], ": ", x
        elif i != '':
            "You selected", datatypes[j], ": ", i
        j += 1

with col2:
    folium_static(map.m)

if st.button('Find Places'):
    "I want to die"