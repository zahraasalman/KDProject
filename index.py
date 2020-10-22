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


def options():  # lets user ppipreqs /home/project/locationick the country/region/continent/capital
    return_list = {}  # dictionary
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
            "No results found, please try another option!"

    if st.checkbox("Filter by Region"):
        option_region = st.selectbox(
            'Which Region?',
            Q.get_regions(continent))

        if option_region:
            return_list["region"] = option_region
            region = option_region
        else:
            "No results found, please try another option!"

    option_country = st.selectbox(
        'Which country?',
        Q.get_countries(continent, region))
    return_list["country"] = option_country
    country = option_country

    if st.checkbox("Select Capital"):
        option_capital = st.selectbox(
            'Which capital?',
            Q.get_capitals(country))

        if option_capital:
            return_list["capital"] = option_capital
        else:
            "No results found, please try another option!"

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
    results_from_funoptions = options()
    for key, value in results_from_funoptions.items():
        "You selected " + key + ": " + value

with col2:
    folium_static(map.m)

if st.button('Find Places'):
    pass  ## redirect to page blabla
