from node import Node
from edge import Edge
import coordinate



def create_node_from_navitia(response):
    # load data from first journey from navitia
    nodes = []
    journey = response['journeys'][0]
    temp = journey['sections'][0]['from']

    # add first node
    node = calculate_node_coord_from_navitia(temp)
    nodes.append(node)

    # add other nodes
    for section in journey["sections"]:
        if section['type'] != "waiting" and section['type'] != "transfer":
            temp = section['to']
            node = calculate_node_coord_from_navitia(temp)
            nodes.append(node)
        elif(section['type']=="transfer"):
            if section['from']['name'] != section['to']['name']:
                temp = section['to']
                node = calculate_node_coord_from_navitia(temp)
                nodes.append(node)
    return nodes

def calculate_node_coord_from_navitia(src):
    if src['embedded_type'] == "address":
        node = Node(src['id'], src['name'])
    elif src['embedded_type'] == "stop_point":
        coord = coordinate.get_coordinates_string(coordinate.get_coordinates(src['name']))
        node = Node(coord, src['name'])
    return node

def set_edge_info(section, edge):
    if(section['type']=="street_network"):
        if (section['mode']=='walking'):
            edge.set_type("walking")
    if(section['type']=="public_transport"):
        if section['display_informations']['commercial_mode'] == 'Métro':
            edge.set_type("metro")
        if section['display_informations']['commercial_mode'] == 'Bus':
            edge.set_type("bus")
        if section['display_informations']['commercial_mode'] == 'commercial_mode':
            edge.setTyp('tramway')
        if section['display_informations']['commercial_mode'] == 'RER' and section['display_informations']['network'] == 'RER':
            edge.set_type("rer")
        if section['display_informations']['commercial_mode'] == 'RER' and section['display_informations']['network'] == 'Transilien':
            edge.set_type("transilien")
            edge.set_line(section['display_informations']['code']).set_description("to " + section['display_informations']['direction'])
        

def create_edges_from_navitia(response, graph):
    journey = response['journeys'][0]
    edges = []
    # add edges

    for section in journey["sections"]:
        if section['type'] != "waiting" and section['type'] != "transfer":

            src = calculate_node_coord_from_navitia(section['from'])
            dest = calculate_node_coord_from_navitia(section['to'])
            if graph.find_node_from_coord(src.coord) and graph.find_node_from_coord(dest.coord):
                    edge = Edge(graph.find_node_from_coord(src.coord),graph.find_node_from_coord(dest.coord), section['duration'], section['duration'])
                    set_edge_info(section, edge)
                    edges.append(edge)
        elif section['type']=="transfer":
            if(section['from']['name'] != section['to']['name']):
                src = calculate_node_coord_from_navitia(section['from'])
                dest = calculate_node_coord_from_navitia(section['to'])
                if graph.find_node_from_coord(src.coord) and graph.find_node_from_coord(dest.coord):
                    edge = Edge(graph.find_node_from_coord(src.coord), graph.find_node_from_coord(dest.coord), section['duration'],
                                section['duration'])
                    set_edge_info(section, edge)
                    edges.append(edge)
    return edges