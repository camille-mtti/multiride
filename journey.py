import requests
import json
from graph import Graph
from dotenv import load_dotenv
from os import getenv
load_dotenv()



def get_navitia_journey(source, dest):
    r = requests.get('https://api.navitia.io/v1/coverage/fr-idf/journeys?from=' + source + '&to=' + dest,
      auth=(getenv("NAVITIA_TOKEN"), ''))
    response = json.loads(r.text)
    graph = Graph()
    graph.create_node_from_navitia(response)
    return graph.nodes
