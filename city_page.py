import streamlit as st
import queries as Q


def show(city=None):
    cityName = city.replace("%20", " ")
    st.title(cityName)

    ### QUERIES ###
    landmarks = Q.get_city_landmarks(city)
    theaters = Q.get_city_theaters(city)
    markets = Q.get_city_markets(city)
    themeParks = Q.get_city_theme_parks(city)
    parks = Q.get_city_parks(city)

    # print(landmarks, theaters, markets, themeParks, parks)

    if landmarks:
        result = ""
        for landmark in landmarks[-1]:
            print(landmark)
            result += landmark[0][1] + ", "
        else:
            result += ". "

        st.markdown('**Landmarks:** ' + result)

    if theaters:
        result = ""
        for theater in theaters[-1]:
            result += theater + ", "
        else:
            result += theater + ". "

        st.markdown('**Theaters:** ' + result)

    if markets:
        result = ""
        for market in markets[-1]:
            result += market + ", "
        else:
            result += market + ". "

        st.markdown('**Markets:** ' + result)

    if parks:
        result = ""
        for park in parks[-1]:
            result += park + ", "
        else:
            result += park + ". "

        st.markdown('**Parks:** ' + result)

    if themeParks:
        result = ""
        for themePark in themeParks[-1]:
            result += themePark + ", "
        else:
            result += themePark + ". "

        st.markdown('**Theme Parks:** ' + result)
