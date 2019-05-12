import requests
import json
from node import Node
import coordinate


def create_node(response):
    nodes = []
    journey = response['journeys'][0]
    temp = journey['sections'][0]['from']
    if(temp['embedded_type'] == "address"):
        node = Node(temp['id'], temp['name'])
    elif(temp['embedded_type'] == "stop_point"):
        coord = coordinate.get_coordinates_string(
            coordinate.get_coordinates(temp['name']))
        node = Node(coord, temp['name'])
    nodes.append(node)
    for section in journey["sections"]:
        if(section['type'] != "waiting" and section['type'] != "transfer"):
            temp = section['to']
            if(temp['embedded_type'] == "address"):
                node = Node(temp['id'], temp['name'])
            elif(temp['embedded_type'] == "stop_point"):
                coord = coordinate.get_coordinates_string(coordinate.get_coordinates(temp['name']))
                node = Node(coord, temp['name'])
            nodes.append(node)
    print('mes nodes : ')
    for n in nodes:
        print(n.coord+"  "+n.address)
    return nodes


def get_navitia_journey(source, dest):
    r = requests.get('https://api.navitia.io/v1/coverage/fr-idf/journeys?from=' + source + '&to=' + dest,
                     auth=('be72cc2c-e6eb-4628-9a88-b7c54746c61a', ''))
    response = json.loads(r.text)
    create_node(response)
    return response
