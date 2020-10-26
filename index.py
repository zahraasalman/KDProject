import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import folium_static
import city_page
import country_page
import re

import folium as f
from streamlit_folium import folium_static

import map as M
import queries as Q

# define pages
PAGES = {
    'countryDetail': country_page,
    'cityDetail': city_page
}


############################### FUNCTIONS ######################################
def _max_width_():  # CSS to make screen in wide mode
    max_width_str = f"max-width: 1200px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
        display: inline;
        justify-content: center;

    }}
    </style>
    """,
        unsafe_allow_html=True,
    )


def background():  # CSS to change background
    max_width_str = f"max-width: 2000px;"
    st.markdown(
        """
    <style>
    .reportview-container .main .block-container{
        justify-content: center;
    }
    body {
        background-color: #141414;
    }
    p {color: #04b4a8;}
    h2, h3, h4, h5, h6 {font-family:serif; color: #dadce7}
    h1{
        color :#66fcf1;
        text-align: center;
    }
    .Widget > label {
        color: #04b4a8;
        color: #04b4a8;
        # max-width: 50%;
        }
    .st-at {
        background-color: #f1f2f6;
    }
    .st-b7 {
        # width: 70%;
    }
    [class^="st-b"]  { color: #14A098;}
    .reportview-container .element-container {color: white;}
    element.style {
        color: white;
    }
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
    options.filter_by_capital = False
    options.custom_coordinates = False
    continent = 'all'
    region = 'all'
    country = 'all'

    if st.checkbox("Enable custom coordinates"):
        options.custom_coordinates = True
        user_input = [(st.number_input("Latitude"), st.number_input("Longtitude"))]
        options.user_coordinates = user_input

    if st.checkbox("Filter by Continent"):
        continents = {'continent': [], 'label': []}
        result_list = Q.get_continents()
        if result_list == []:
            st.markdown("<font color='red' face='monospace' size='+1'><b>"
                        "No results found, please try another option!"
                        "</b></font>", unsafe_allow_html=True)
        else:
            for cont in result_list:
                continents['continent'].append(cont[0])
                continents['label'].append(cont[1])
            option_continent = st.selectbox(
                'Which continents?',
                sorted(continents['label']))

            if option_continent:
                return_list['continent'] = option_continent
                index = find_index(option_continent, continents['label'])
                continent = continents['continent'][index]
            else:
                if result_list == []:
                    st.markdown("<font color='red' face='monospace' size='+1'><b>"
                                "No results found, please select a continent or unselect the checkbox!"
                                "</b></font>", unsafe_allow_html=True)

    if st.checkbox("Filter by Region"):
        regions = {'region': [], 'label': []}
        result_list = Q.get_regions(continent)
        if result_list == []:
            st.markdown("<font color='red' face='monospace' size='+1'><b>"
                        "No results found, please try another option!"
                        "</b></font>", unsafe_allow_html=True)
        else:
            for reg in result_list:
                regions['region'].append(reg[0])
                regions['label'].append(reg[1])
            option_region = st.selectbox(
                'Which Region?',
                sorted(regions['label']))

            if option_region:
                return_list['region'] = option_region
                index = find_index(option_region, regions['label'])
                region = regions['region'][index]
            else:
                st.markdown("<font color='red' face='monospace' size='+1'><b>"
                            "No results found, please select a region or unselect the checkbox!"
                            "</b></font>", unsafe_allow_html=True)

    countries = {'country': [], 'label': []}
    for count in Q.get_countries(continent, region):
        countries['country'].append(count[0])
        countries['label'].append(count[1])
    option_country = st.selectbox(
        'Which country?',
        sorted(countries['label']))

    if option_country:  ## if there is an option, then we save it in the list
        return_list["country"] = option_country
        index = find_index(option_country, countries['label'])
        country = countries['country'][index]
        options.country = country  # individual or label?
    else:
        st.markdown("<font color='red' face='monospace' size='+1'><b>"
                    "No results found..."
                    "</b></font>", unsafe_allow_html=True)

    if st.checkbox("Select Capital"):
        options.filter_by_capital = True
        capitals = {'capital': [], 'label': []}
        result_list = Q.get_capitals(country)
        if result_list == []:
            st.markdown("<font color='red' face='monospace' size='+1'><b>"
                        "No results found, please try another option!"
                        "</b></font>", unsafe_allow_html=True)
        else:
            for cap in result_list:
                capitals['capital'].append(cap[0])
                capitals['label'].append(cap[1])
            option_capital = st.selectbox(
                'Which capital?',
                sorted(capitals['label']))

            if option_capital:
                return_list["capital"] = option_capital
                index = find_index(option_capital, capitals['label'])
                capital = capitals['capital'][index]
                options.capital = capital  # individual or label?
            else:
                st.markdown("<font color='red' face='monospace' size='+1'><b>"
                            "No results found, please select a capital or unselect the checkbox!"
                            "</b></font>", unsafe_allow_html=True)

    return return_list

def get_cities(country):
    cities = Q.get_country_cities(country)
    cities_utilities_list = []
    for city in cities:
        label = city
        coordinates = Q.get_city_coordinates(city)
        if coordinates == []:
            coordinates = None
            print(label)
            print(coordinates)
        cities_utilities_list.append(tuple((label, coordinates)))
    return cities_utilities_list



############################### INTRODUCTION ####################################
_max_width_()
background()
st.title("WELCOME TO <APP NAME>")
"""
This app is made to help you get your information before you travel to your touisty destination blah blah idc. \n
This is multi-line and it's awesome
"""
col1, col2 = st.beta_columns([2, 3])

with col1:
    st.subheader("Please select the country or city that you want to view")
    """

    """
    results_from_funoptions = options()
    for key, value in results_from_funoptions.items():
        "You selected " + key + ": " + value

with col2:
    if not options.custom_coordinates:  # Experimental feature to insert custom coordinates to test certain spots on the map.
        if not options.filter_by_capital:  # Filters by country if capital filtering is not specified.
            try:
                try:
                    cities_utilities = get_cities(options.country)
                    print(cities_utilities)
                except:
                    "Cities unable to be retrieved"
                cords = str(Q.get_country_coordinates(options.country)[0])
                cords = re.split('\(|\)| ', cords)
                M.getMap([(cords[2], cords[1])], 4, cities_utilities)
            except:
                st.markdown("<font color='red' face='monospace' size='+2'><b>"
                            "Oops! It appears that our external databases do not yet contain the coordinates of this country."
                            "This doesn't mean your option is invalid, please continue."
                            "</b></font>", unsafe_allow_html=True)
        else:  # Filter by capital
            try:
                cords = Q.get_capital_coordinates(options.capital)
                M.getMap(cords, 12)
            except:
                st.markdown("<font color='red' face='monospace' size='+2'><b>"
                            "Oops! It appears that our external databases do not yet contain the coordinates of this country."
                            "This doesn't mean your option is invalid, please continue"
                            "</b></font>", unsafe_allow_html=True)
    else:  # Check inserted coordinates on the map.
        M.getMap(options.user_coordinates, 4)

# I have decided to place the col2 in the button function, the map will now appear as the user gives input.

if st.button('Find Places'):
    if hasattr(options, 'capital'):
        PAGES['cityDetail'].show(city=options.capital)
    else:
        PAGES['countryDetail'].show(country=options.country)
