import requests
import json
import navitia
from graph import Graph
from uber import Uber
from dotenv import load_dotenv
from os import getenv
load_dotenv()


def get_journey(source, dest, price):
    print("beginning of algorithm")
    r = requests.get(
      'https://api.navitia.io/v1/coverage/fr-idf/journeys?from=' + source + '&to=' + dest,
      auth=(getenv("NAVITIA_TOKEN"), '')
    )
    response = json.loads(r.text)

    graph = Graph()

    uber = Uber()

    graph.add_nodes(navitia.create_node_from_navitia(response))
    graph.add_edges(navitia.create_edges_from_navitia(response, graph))

    graph.add_edges(uber.create_uber_trajects(graph, price))
    print("---------------------------- PRINT GRAPH ----------------------------------------------")
    graph.print_nodes()
    graph.print_edges()

    traject = graph.dijkstra(graph.nodes[0], graph.nodes[len(graph.nodes) - 1], price)
    return traject
