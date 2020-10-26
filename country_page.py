import streamlit as st
import queries as Q


def show(country=None):
    st.title(country)

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
                    newValue = value.replace("%20", " ")
                    st.markdown('**' + key + ":** " + newValue)

        if languages:
            result = ""
            for language in languages[:-1]:
                result += language + ", "
            else:
                result += language + ". "
            if result != '':
                st.markdown('**Languages:** ' + result)

        if currency:
            st.markdown('**Currency:** ' + currency[0][1])

        if nationalDish:
            st.markdown('**National Dish:** ' + nationalDish[0][1])

        if nationalAnimalPlant:
            st.markdown('**National animal or plant:** ' + nationalAnimalPlant)

        if food:
            result = ""

            for f in food[:-1]:
                result += f[0][1] + ", "
            else:
                if result != '':
                    result += ". "
            if result != '':
                st.markdown('**Food:** ' + result)

        if resortTowns:
            result = ""

            for town in resortTowns[:-1]:
                result += town[0][1] + ", "
            else:
                result += town + ". "
            if result != '':
                st.markdown('**Resort Towns:** ' + result)


        if landmarks:
            result = ""

            for landmark in landmarks[:-1]:
                print(landmark)
                result += landmark[0][1] + ", "
            else:
                result += landmark[0][1] + ". "
            if result != '':
                st.markdown('**Landmarks:** ' + result)

        if neighbours:
            result = ""

            for neighbour in neighbours[:-1]:
                result += neighbour + ", "
            else:
                result += neighbour + ". "
            if result != '':
                st.markdown('**Neighbouring countries (recommended to check):** *' + result)
                st.markdown('* In the full implemented version, these will be hyperlinks to go to the country pages'
                            + result)

        if cities:
            result = ""

            for city in cities[:-1]:
                result += city + ", "
            else:
                result += city + ". "
            if result != '':
                st.markdown('**Cities:** ' + result)
