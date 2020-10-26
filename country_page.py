import streamlit as st
import queries as Q


def show(country=None):
    st.title(country)

    ### QUERIES ###
    countyInfo = Q.get_country_basic_info(country)
    languages = Q.get_country_languages(country)
    currency = Q.get_country_currency(country)
    nationalDish = Q.get_country_national_dish(country)
    nationalAnimalPlant = Q.get_country_national_animal_plant(country)
    food = Q.get_country_food(country)

    resortTowns = Q.get_country_resort_towns(country)
    landmarks = Q.get_country_landmarks(country)

    neighbours = Q.get_country_neighbors(country)
    cities = Q.get_country_cities(country)

    st.markdown('** General Info **')

    if countyInfo:
        if country.abstract:
            st.write(''' Abstract:  ''')
            st.write(country.abstract)

        if country.flag:
            st.write(''' Flag:  ''')
            st.write(country.flag)

        if country.capital:
            st.write(''' Capital city:  ''')
            st.write(country.capital)

        if country.population:
            st.write(''' Population:  ''')
            st.write(country.population)

    if languages:
        st.write(''' Languages:  ''')

        for language in languages:
            st.write(language + ", ")

    if currency:
        st.write(''' Currency:  ''')
        st.write(currency)

    if nationalDish:
        st.write(''' National Dish:  ''')
        st.write(nationalDish)

    if nationalAnimalPlant:
        st.write(''' National animal or plant:  ''')
        st.write(nationalAnimalPlant)

    if food:
        st.write(''' Food:  ''')

        for f in food:
            st.write(f + ", ")

    if resortTowns:
        st.write(''' Resort Towns:  ''')

        for town in resortTowns:
            st.write(town + ", ")

    if landmarks:
        st.write(''' Landmarks:  ''')

        for landmark in landmarks:
            st.write(landmark + ", ")

    if cities:
        st.write(''' Main cities:  ''')

        for city in cities:
            st.write(city + ", ")

    if neighbours:
        st.write(country + ''' neighbours:  ''')

        for neighbour in neighbours:
            st.write(neighbour + ", ")
