import streamlit as st
import queries as Q


def show(city=None, cityName=None):
    st.title(cityName)

    ### QUERIES ###
    cityInfo = Q.get_city_basic_info(city)
    population = Q.get_city_population(city)
    landmarks = Q.get_city_landmarks(city)
    theaters = Q.get_city_theaters(city)
    # markets = Q.get_city_markets(city)
    themeParks = Q.get_city_theme_parks(city)
    parks = Q.get_city_parks(city)

    # print(landmarks, theaters, markets, themeParks, parks)

    col1, col2 = st.beta_columns([3, 2])
    with col1:
        if cityInfo:
            st.markdown(cityInfo['Abstract'])

    with col2:
        if landmarks:
            result = ""
            for landmark in landmarks:
                result += landmark + ", "

            st.markdown('**Landmarks:** ' + result[:-2] + ". ")

        if theaters:
            result = ""
            for theater in theaters:
                result += theater + ", "

            st.markdown('**Theaters:** ' + result[:-2] + ". ")

        # query doesn't work
        # if markets:
        #     result = ""
        #     for market in markets:
        #         print()
        #         print(market)
        #         result += market + ", "
        #
        #     st.markdown('**Markets:** ' + result[:-2] + ". ")

        if parks:
            result = ""
            for park in parks:
                print()
                print(park)
                result += park + ", "

            st.markdown('**Parks:** ' + result[:-2] + ". ")

        if themeParks:
            result = ""
            for themePark in themeParks:
                result += themePark + ", "

            st.markdown('**Theme Parks:** ' + result[:-2] + ". ")
