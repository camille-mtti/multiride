import requests
import json
import navitia
from graph import Graph
from dotenv import load_dotenv
from os import getenv
load_dotenv()



def get_navitia_journey(source, dest):
    r = requests.get('https://api.navitia.io/v1/coverage/fr-idf/journeys?from=' + source + '&to=' + dest,
      auth=(getenv("NAVITIA_TOKEN"), ''))
    response = json.loads(r.text)
    print(response)
    graph = Graph()
    graph.add_nodes(navitia.create_node_from_navitia(response))
    graph.add_edges(navitia.create_edges_from_navitia(response, graph))
    graph.print_nodes()
    graph.print_edges()
    return graph.nodes
