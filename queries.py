import rdflib
import SPARQLWrapper
from rdflib import Graph, RDF, Namespace, Literal, URIRef
from SPARQLWrapper import SPARQLWrapper, JSON


# sparql = SPARQLWrapper("https://kdp-roject-zahraasalman.projectkd.vercel.app/")
sparql = SPARQLWrapper("http://192.168.1.110:7200/repositories/FinalProject")


def get_continents():
    result_list = []
    sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX : <http://www.tourism.org/group6/>
        select ?continent where { 
            ?continent rdf:type :Continent
        }
        """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        result = result["continent"]["value"].split('/')[-1]
        result = result.replace("%20", " ")
        result_list.append(result)

    if result_list == []:
        result_list = "No results found, please try another option!"
    return result_list


def get_regions(continent='all'):
    result_list = []
    continent = continent.replace(" ", "%20")

    if continent == 'all':  # continent is not selected so show all regions
        sparql.setQuery("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX : <http://www.tourism.org/group6/>
            select ?region where { 
                ?country rdf:type :Country;
                         :fromContinent ?continent;
                         :fromRegion ?region.        
            }GROUP BY (?region)
            """)
    else: # continent is selected
        sparql.setQuery("""
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX : <http://www.tourism.org/group6/>
                select ?region where { 
                ?country rdf:type :Country;
                         :fromContinent :%s;
                         :fromRegion ?region.        
                }GROUP BY (?region)
                """ % continent)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        result = result["region"]["value"].split('/')[-1]
        result = result.replace("%20", " ")
        result_list.append(result)

    if result_list == []:
        result_list = "No results found, please try another option!"
    return result_list


def get_countries(continent='all', region='all'):
    result_list = []
    continent = continent.replace(" ", "%20")
    region = region.replace(" ", "%20")

    if continent == 'all' and region == 'all':  # default aka neither region nor continent is selected
        sparql.setQuery("""
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX : <http://www.tourism.org/group6/>
                select ?country where { 
                    ?country rdf:type :Country
                }
                """)
    elif continent != 'all' and region == 'all':  # continent is selected but not region
        sparql.setQuery("""
                        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                        PREFIX : <http://www.tourism.org/group6/>
                        select ?country where { 
                            ?country rdf:type :Country;
                                    :fromContinent :%s.
                        }
                        """ % continent)
    elif continent == 'all' and region != 'all':  # region is selected but not continent
        sparql.setQuery("""
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX : <http://www.tourism.org/group6/>
                select ?country where { 
                    ?country rdf:type :Country;
                            :fromRegion :%s.
                        }
                """ % region)
    elif continent != 'all' and region != 'all':  # both region and continent are selected
        sparql.setQuery("""
                        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                        PREFIX : <http://www.tourism.org/group6/>
                        select ?country where { 
                            ?country rdf:type :Country;
                                    :fromContinent :%s;
                                    :fromRegion :%s.
                        }
                        """ % (continent, region))

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        result = result["country"]["value"].split('/')[-1]
        result = result.replace("%20", " ")
        result_list.append(result)

    if result_list == []:
        result_list = "No results found, please try another option!"
    return result_list


def get_capitals(country):  # could be changed to get cities
    result_list = []
    country = country.replace(" ", "%20")

    sparql.setQuery("""
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX : <http://www.tourism.org/group6/>
                    select ?capital where { 
                        ?capital rdf:type :Capital;
                                :fromCountry :%s . 
                    } 
                    """ % country)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        result = result["capital"]["value"].split('/')[-1]
        result = result.replace("%20", " ")
        result_list.append(result)

    if result_list == []:
        result_list = "No results found, please try another option!"
    return result_list


def get_country_coordinates(country):
    result_list = []
    country = country.replace(" ", "%20")

    sparql.setQuery("""
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX : <http://www.tourism.org/group6/>
                    select * where { 
                            :%s :hasLatitude ?lat;
                                :hasLongitude ?long.
                    } 
                    """ % country)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        result1 = float(result["lat"]["value"])
        result2 = float(result["long"]["value"])
        if [result1, result2] not in result_list:
            result_list.append([result1, result2])

    if result_list == []:
        result_list = "No results found, please try another option!"
    return result_list


###################### TESTING THE FUNCTIONS ##############################
# print(get_continents())
# print(get_countries(region="Southern%20Europe"))
# print(get_regions("Europe"))
# print(get_capitals("Netherlands"))
print(get_country_coordinates("Mexico"))
