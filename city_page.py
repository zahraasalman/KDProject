import streamlit as st
import queries as Q


def show(city=None):
    st.title(city)

    ### QUERIES ###
    landmarks = Q.get_city_landmarks(city)
    theaters = Q.get_city_theaters(city)
    markets = Q.get_city_markets(city)
    themeParks = Q.get_city_theme_parks(city)
    parks = Q.get_city_parks(city)

    st.markdown('** Info **')

    if landmarks:
        st.write(''' Landmarks:  ''')

        for landmark in landmarks:
            st.write(landmark + ", ")

    if theaters:
        st.write(''' Theaters:  ''')

        for theater in theaters:
            st.write(theaters + ", ")

    if markets:
        st.write(''' Markets:  ''')

        for market in markets:
            st.write(markets + ", ")

    if parks:
        st.write(''' Parks:  ''')

        for park in parks:
            st.write(park + ", ")

    if themeParks:
        st.write(''' Theme Parks:  ''')

        for themePark in themeParks:
            st.write(themePark + ", ")
