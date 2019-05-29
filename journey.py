import requests
import json
from graph import Graph

def get_navitia_journey(source, dest):
    r = requests.get('https://api.navitia.io/v1/coverage/fr-idf/journeys?from=' + source + '&to=' + dest,
                     auth=('be72cc2c-e6eb-4628-9a88-b7c54746c61a', ''))
    response = json.loads(r.text)
    nodes = Graph.create_node_from_navitia(response)
    return nodes
