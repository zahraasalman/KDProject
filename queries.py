import rdflib
import SPARQLWrapper
from rdflib import Graph, RDF, Namespace, Literal, URIRef
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://192.168.1.103:7200/repositories/FinalProject")


def get_continents():
    result_list = []
    sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX : <http://www.tourism.org/group6/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        select * where { 
            ?continent rdf:type :Continent;
                        rdfs:label ?continentlabel.
        }
        """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        continent = result["continent"]["value"].split('/')[-1]
        continentlabel = result["continentlabel"]["value"]

        result_list.append((continent, continentlabel))

    return result_list


def get_regions(continent='all'):
    result_list = []

    if continent == 'all':  # continent is not selected so show all regions
        sparql.setQuery("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX : <http://www.tourism.org/group6/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            select distinct ?region ?regionlabel where { 
                ?country rdf:type :Country;
                         :fromContinent ?continent;
                         :fromRegion ?region.      
                ?region rdfs:label ?regionlabel.  
            }
            """)
    else:  # continent is selected
        sparql.setQuery("""
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX : <http://www.tourism.org/group6/>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                select distinct ?region ?regionlabel where { 
                ?country rdf:type :Country;
                         :fromContinent :%s;
                         :fromRegion ?region.   
                ?region rdfs:label ?regionlabel.       
                }
                """ % continent)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        region = result["region"]["value"].split('/')[-1]
        regionlabel = result["regionlabel"]["value"]
        result_list.append((region, regionlabel))
    return result_list


def get_countries(continent='all', region='all'):
    result_list = []
    continent = continent.replace(" ", "%20")
    region = region.replace(" ", "%20")

    if continent == 'all' and region == 'all':  # default aka neither region nor continent is selected
        sparql.setQuery("""
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX : <http://www.tourism.org/group6/>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                select ?country ?countrylabel where { 
                    ?country rdf:type :Country;
                            rdfs:label ?countrylabel.
                }
                """)
    elif continent != 'all' and region == 'all':  # continent is selected but not region
        sparql.setQuery("""
                        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                        PREFIX : <http://www.tourism.org/group6/>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                        select ?country ?countrylabel where { 
                            ?country rdf:type :Country;
                                    rdfs:label ?countrylabel;
                                    :fromContinent :%s.
                        }
                        """ % continent)
    elif continent == 'all' and region != 'all':  # region is selected but not continent
        sparql.setQuery("""
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX : <http://www.tourism.org/group6/>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                select ?country ?countrylabel where { 
                    ?country rdf:type :Country;
                            rdfs:label ?countrylabel;
                            :fromRegion :%s.
                        }
                """ % region)
    elif continent != 'all' and region != 'all':  # both region and continent are selected
        sparql.setQuery("""
                        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                        PREFIX : <http://www.tourism.org/group6/>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                        select ?country ?countrylabel where { 
                            ?country rdf:type :Country;
                                    rdfs:label ?countrylabel;
                                    :fromContinent :%s;
                                    :fromRegion :%s.
                        }
                        """ % (continent, region))

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        country = result["country"]["value"].split('/')[-1]
        countrylabel = result["countrylabel"]["value"]
        result_list.append((country, countrylabel))

    return result_list


def get_capitals(country):  # could be changed to get cities
    result_list = []
    country = country.replace(" ", "%20")

    sparql.setQuery("""
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX : <http://www.tourism.org/group6/>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    
                    select ?capital ?capitallabel where { 
                        :%s :hasCapital ?capital.
                        ?capital rdfs:label ?capitallabel.
                    } 
                    """ % country)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        capital = result["capital"]["value"].split('/')[-1]
        capitallabel = result["capitallabel"]["value"]
        result_list.append((capital, capitallabel))

    return result_list


def get_country_coordinates(country):
    # The coordinates are fucked, probably a faulty css or an import error from GraphDB
    # Mexico is the only working version, the rest is borked, wil investigate tomorrow. (23 okt)
    result_list = []

    sparql.setQuery("""
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX : <http://www.tourism.org/group6/>
                    select * where { 
                            :%s :hasCoordinates ?cordinates.
                    } 
                    """ % country)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        result1 = str(result["cordinates"]["value"])
        if [result1] not in result_list:
            result_list.append([result1])

    return result_list


def get_capital_coordinates(capital):
    result_list = []
    capital = capital.replace(" ", "%20")

    sparql.setQuery("""
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX : <http://www.tourism.org/group6/>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    select * where { 
                            :%s rdf:type :Capital;
                                :hasLatitude ?lat;
                                :hasLongitude ?long.
                    } 
                    """ % capital)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        result1 = float(result["lat"]["value"])
        result2 = float(result["long"]["value"])
        if [result1, result2] not in result_list:
            result_list.append([result1, result2])

    return result_list


###COUTRY QUERIES
def get_country_basic_info(country):
    result_list = {}
    country = country.replace(" ", "%20")

    sparql.setQuery("""
                       PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                       PREFIX ex: <http://www.tourism.org/group6/>
                       
                       select * where {
                            ex:%s rdf:type ex:Country;
                                  ex:hasAbstract ?abstract;
                                  ex:hasFlag ?flag;
                                  ex:hasCapital ?capital;
                                  ex:hasPopulation ?population.
                        }

                        """ % country)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        abstract = result["abstract"]["value"]
        flag = result["flag"]["value"]
        capital = result["capital"]["value"].split('/')[-1]
        population = result["population"]["value"]

        result_list['Abstract'] = abstract
        result_list['Flag'] = flag
        result_list['Capital'] = capital
        result_list['Population'] = population

    return result_list


##TODO: does not work, please fix?
def get_country_neighbors(country):
    pass
    # result_list = []
    # country = country.replace(" ", "%20")
    #
    # sparql.setQuery("""
    #                   PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    #                   PREFIX ex: <http://www.tourism.org/group6/>
    #
    #                   select * where {
    #                      ex:%s ex:sharesBordersWith ?neighboringcountry.}
    #                     """ % country)
    #
    # sparql.setReturnFormat(JSON)
    # results = sparql.query().convert()
    #
    # for result in results["results"]["bindings"]:
    #     neighbor = result["neighboringcountry"]["value"]
    #     result_list.append(neighbor)
    #
    # return result_list


def get_country_languages(country):
    result_list = []
    country = country.replace(" ", "%20")

    sparql.setQuery("""
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX ex: <http://www.tourism.org/group6/>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

                    select * where {
                        ex:%s rdf:type ex:Country;
                              ex:hasLanguage ?language.

                        ?language rdfs:label ?languagelabel.
                    }
                     """ % country)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        # language = result["language"]["value"]
        languageLabel = result["languagelabel"]["value"]
        result_list.append(languageLabel)

    return result_list


def get_country_currency(country):
    result_list = []
    country = country.replace(" ", "%20")

    sparql.setQuery("""
                        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                        PREFIX ex: <http://www.tourism.org/group6/>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

                        select * where {
                            ?currency rdf:type ex:Currency;
                                    ex:fromCountry ex:%s;
                                    ex:hasCurrencyCode ?currencycode.

                            ?currency rdfs:label ?currencylabel.
                            ?currencycode rdfs:label ?currencycodelabel.
                        }
                     """ % country)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        currency = result["currency"]["value"]
        currencyLabel = result["currencylabel"]["value"]
        result_list.append((currency, currencyLabel))

    return result_list


def get_country_cities(country):
    result_list = []
    country = country.replace(" ", "%20")

    sparql.setQuery("""
                        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                        PREFIX ex: <http://www.tourism.org/group6/>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

                        select * where {
                            ex:%s rdf:type ex:Country;
                                        ex:hasCity ?city.

                            ?city rdfs:label ?citylabel.
                        }
                     """ % country)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        # city = result["city"]["value"].split('/')[-1]
        cityLabel = result["citylabel"]["value"]
        result_list.append(cityLabel)

    return result_list


def get_country_landmarks(country):
    result_list = []
    country = country.replace(" ", "%20")

    sparql.setQuery("""
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX ex: <http://www.tourism.org/group6/>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

                select * where {
                	?landmark rdf:type ex:Landmark;
                           ex:fromCountry ex:%s;
                           ex:fromCity ?city;
                           rdfs:label ?landmarklabel;
                           ex:hasCoordinates ?landmarkcoordinates.

                    ?city rdfs:label ?citylabel.
                }
                     """ % country)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        landmark = result["landmark"]["value"]
        landmarkLabel = result["landmarklabel"]["value"]
        result_list.append((landmark, landmarkLabel))

    return result_list


def get_country_national_dish(country):
    result_list = []
    country = country.replace(" ", "%20")

    sparql.setQuery("""
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX ex: <http://www.tourism.org/group6/>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

                select * where {
                        ?nationaldish rdf:type ex:National_Dish;
                                      ex:fromCountry  ex:%s;
                                      rdfs:label ?nationaldishlabel.
                }
                         """ % country)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        nationalDish = result["nationaldish"]["value"]
        nationalDishLabel = result["nationaldishlabel"]["value"]
        result_list.append((nationalDish, nationalDishLabel))

    return result_list


def get_country_national_animal_plant(country):
    result_list = []
    country = country.replace(" ", "%20")

    sparql.setQuery("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX ex: <http://www.tourism.org/group6/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

            select * where {
                ?nationalanimalorplant rdf:type ex:National_Animal_Or_Plant;
                       ex:fromCountry ex:%s;
                       rdfs:label ?nationalanimalorplantlabel.
            }
                         """ % country)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        nationalAnimalPlant = result["nationalanimalorplant"]["value"]
        nationalAnimalPlantLabel = result["nationalanimalorplantlabel"]["value"]
        result_list.append((nationalAnimalPlant, nationalAnimalPlantLabel))

    return result_list


def get_country_food(country):
    result_list = []
    country = country.replace(" ", "%20")

    sparql.setQuery("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX ex: <http://www.tourism.org/group6/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

            select * where {
                ?food rdf:type ex:Food;
                       ex:fromCountry ex:%s;
                       rdfs:label ?foodlabel.

                FILTER (!EXISTS {?food rdf:type ex:National_Dish})
                }
                         """ % country)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        food = result["food"]["value"]
        foodLabel = result["foodlabel"]["value"]
        result_list.append((food, foodLabel))

    return result_list


def get_country_resort_towns(country):
    result_list = []
    country = country.replace(" ", "%20")

    sparql.setQuery("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX ex: <http://www.tourism.org/group6/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

            select * where {
                ?resorttown rdf:type ex:ResortTown;
                       ex:fromCountry ex:%s;
                       rdfs:label ?resorttownlabel;
                       ex:hasCoordinates ?resorttowncoordinates.
            }
                         """ % country)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        resortTown = result["resorttown"]["value"]
        resortTowLabel = result["resorttownlabel"]["value"]
        result_list.append((resortTown, resortTowLabel))

    return result_list


## CAPITAL PAGE

def get_city_landmarks(capital):
    result_list = []
    capital = capital.replace(" ", "%20")

    sparql.setQuery("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX ex: <http://www.tourism.org/group6/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

            select * where {
                ?landmark rdf:type ex:Landmark;
                       ex:fromCity ex:%s;
                       rdfs:label ?landmarklabel;
                       ex:hasCoordinates ?landmarkcoordinates.
            }
                         """ % capital)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        # landmark = result["landmark"]["value"]
        landmarkLabel = result["landmarklabel"]["value"]
        result_list.append(landmarkLabel)

    return result_list


def get_city_theaters(capital):
    result_list = []
    capital = capital.replace(" ", "%20")

    sparql.setQuery("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX ex: <http://www.tourism.org/group6/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX ex2: <http://www.semanticweb.org/ontologies/2010/6/tourism.owl#>

            select * where {
                ?theater rdf:type ex2:Theatre;
                       ex:fromCity ex:%s;
                       rdfs:label ?theaterlabel;
                       ex:hasCoordinates ?theatercoordinates.
            }

            """ % capital)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        # theater = result["theater"]["value"]
        theaterLabel = result["theaterlabel"]["value"]
        result_list.append(theaterLabel)

    return result_list


def get_city_markets(capital):
    result_list = []
    capital = capital.replace(" ", "%20")

    sparql.setQuery("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX ex: <http://www.tourism.org/group6/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

            select * where {
                ?market rdf:type ex:Market;
                       ex:fromCity ex:%s;
                       rdfs:label ?marketlabel;
                       ex:hasCoordinates ?marketcoordinates.
            }
            """ % capital)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        # market = result["market"]["value"]
        marketLabel = result["marketlabel"]["value"]
        result_list.append(marketLabel)

    return result_list


def get_city_parks(capital):
    result_list = []
    capital = capital.replace(" ", "%20")

    sparql.setQuery("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX ex: <http://www.tourism.org/group6/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

            select * where {
                ?park rdf:type ex:Park;
                       ex:fromCity ex:%s;
                       rdfs:label ?parklabel;
                       ex:hasCoordinates ?parkcoordinates.
            }
            """ % capital)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        # park = result["park"]["value"]
        parkLabel = result["parklabel"]["value"]
        result_list.append(parkLabel)

    return result_list


def get_city_theme_parks(capital):
    result_list = []
    capital = capital.replace(" ", "%20")

    sparql.setQuery("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX ex: <http://www.tourism.org/group6/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

            select * where {
                ?themepark rdf:type ex:Theme_Park;
                       ex:fromCity ex:%s;
                       rdfs:label ?themeparklabel;
                       ex:hasCoordinates ?themeparkcoordinates.
            }
            """ % capital)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        # themepark = result["themepark"]["value"]
        themeparkLabel = result["themeparklabel"]["value"]
        result_list.append(themeparkLabel)

    return result_list

###################### TESTING THE FUNCTIONS ##############################
# print(get_continents())
# print(get_countries(region="Southern%20Europe"))
# print(get_regions("Europe"))
# print(get_capitals("Netherlands"))
# print(get_country_coordinates("Mexico"))
