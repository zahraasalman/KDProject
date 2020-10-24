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

    if result_list == []:
        result_list = "No results found, please try another option!"
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

    if result_list == []:
        result_list = "No results found, please try another option!"
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

    if result_list == []:
        result_list = "No results found, please try another option!"
    return result_list


def get_country_coordinates(country):
    # The cordinates are fucked, probably a faulty css or an import error from GraphDB
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

    if result_list == []:
        result_list = "No results found, please try another option!"
    return result_list

def get_capital_coordinates(capital):
    result_list = []
    capital = capital.replace(" ", "%20")

    sparql.setQuery("""
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX : <http://www.tourism.org/group6/>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    select * where { 
                            :%s rdf:type :Country;
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

    if result_list == []:
        result_list = "No results found, please try another option!"
    return result_list


###################### TESTING THE FUNCTIONS ##############################
# print(get_continents())
# print(get_countries(region="Southern%20Europe"))
# print(get_regions("Europe"))
# print(get_capitals("Netherlands"))
# print(get_country_coordinates("Mexico"))
