import streamlit as st
import queries as Q


def show(country=None, countrylabel=None):
    st.title(countrylabel)

    ### QUERIES ###
    countryInfo = Q.get_country_basic_info(country)
    languages = Q.get_country_languages(country)
    currency = Q.get_country_currency(country)
    nationalDish = Q.get_country_national_dish(country)
    nationalAnimalPlant = Q.get_country_national_animal_plant(country)
    food = Q.get_country_food(country)

    resortTowns = Q.get_country_resort_towns(country)
    landmarks = Q.get_country_landmarks(country)

    neighbours = Q.get_country_neighbors(country)
    cities = Q.get_country_cities(country)

    col1, col2 = st.beta_columns([3, 2])

    with col1:
        if countryInfo:
            st.markdown(countryInfo['Abstract'])

    with col2:
        if countryInfo:
            for key, value in countryInfo.items():
                if not key == 'Abstract':
                    if key == 'Capital':
                        pass
                    elif key == 'Capitallabel':
                        st.markdown('**Capital: **' + value)
                    else:
                        st.markdown('**' + key + ":** " + value)

        if languages:
            result = ""
            for language in languages:
                if not any(char.isdigit() for char in language):
                    result += language + ", "
            if result != '':
                st.markdown('**Languages:** ' + result[:-2] + '. ')

        if currency and not any(char.isdigit() for char in currency[0][1]):
            st.markdown('**Currency:** ' + currency[0][1])

        if nationalDish and not any(char.isdigit() for char in nationalDish[0][1]):
            st.markdown('**National Dish:** ' + nationalDish[0][1])

        if nationalAnimalPlant and not any(char.isdigit() for char in nationalAnimalPlant):
            st.markdown('**National animal or plant:** ' + nationalAnimalPlant)

        if food:
            result = ""

            for f in food:
                if any(char.isdigit() for char in f):
                    result += f[1] + ", "
            if result != '':
                st.markdown('**Food:** ' + result[:-2] + '. ')

        if resortTowns:
            result = ""

            for town in resortTowns:
                if not any(char.isdigit() for char in f):
                    result += town[1] + ", "
            if result != '':
                st.markdown('**Resort Towns:** ' + result[:-2] + '. ')

        if landmarks:
            result = ""

            for landmark in landmarks:
                if not any(char.isdigit() for char in landmark):
                    result += landmark[1] + ", "
            if result != '':
                st.markdown('**Landmarks:** ' + result[:-2] + '. ')

        if neighbours:
            result = ""

            for neighbour in neighbours:
                if not any(char.isdigit() for char in neighbour):
                    result += neighbour + ", "
            if result != '':
                st.markdown('**Neighbouring countries (recommended to check):** *' + result[:-2] + ". ")

        if cities:
            result = ""

            for city in cities:
                if not any(char.isdigit() for char in city):
                    result += city + ", "
            if result != '':
                st.markdown('**Cities:** * ' + result[:-2] + '. ')

        if cities or neighbours:
            st.markdown('   *In the full implemented version, these will be hyperlinks to go to the country/city pages')
