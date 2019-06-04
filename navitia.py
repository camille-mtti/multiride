from node import Node
from edge import Edge
import coordinate


# this function creates nodes from navitia response
# for now we only create node for the first journey proposed
# a perspective of amelioration would be to create nodes for the first 3 journeys but we didn't have enough time
# also the multiple API calls to UBER makes the request takes too much time for the nodes of one journey
# to add other journeys we would have needed to reduce uber API calls or to do multithreading or find another solution
def create_node_from_navitia(response):
    # load data from first journey from navitia
    nodes = []
    journey = response['journeys'][0]

    # add first node
    temp = journey['sections'][0]['from']
    node = calculate_node_coord_from_navitia(temp)
    nodes.append(node)

    # add other nodes
    for section in journey["sections"]:
        # we skip section of type waiting because we do not need them
        # section of type transfer are treated after
        if section['type'] != "waiting" and section['type'] != "transfer":
            temp = section['to']
            node = calculate_node_coord_from_navitia(temp)
            nodes.append(node)
        # for section of type transfer, we only add the destination node if it is different than the source node
        elif (section['type'] == "transfer"):
            if section['from']['name'] != section['to']['name']:
                temp = section['to']
                node = calculate_node_coord_from_navitia(temp)
                nodes.append(node)
    return nodes


# navitia does not only return address they also returns some kind of ID for some public transport stops
# this functions return a node created from the data from navitia
def calculate_node_coord_from_navitia(src):
    if src['embedded_type'] == "address":
        node = Node(src['id'], src['name'])
    elif src['embedded_type'] == "stop_point":
        coord = coordinate.get_coordinates_string(coordinate.get_coordinates(src['name']))
        node = Node(coord, src['name'])
    return node


# interpret navitia results for the type of edge
# todo complete edge description
def set_edge_info(section, edge):
    if section['type'] == "street_network":
        if section['mode'] == 'walking':
            edge.set_type("walking")
    if section['type'] == "public_transport":
        if section['display_informations']['commercial_mode'] == 'Métro':
            edge.set_type("metro")
        if section['display_informations']['commercial_mode'] == 'Bus':
            edge.set_type("bus")
        if section['display_informations']['commercial_mode'] == 'commercial_mode':
            edge.setTyp('tramway')
        if section['display_informations']['commercial_mode'] == 'RER' and section['display_informations'][
            'network'] == 'RER':
            edge.set_type("rer")
        if section['display_informations']['commercial_mode'] == 'RER' and section['display_informations'][
            'network'] == 'Transilien':
            edge.set_type("transilien")
            edge.set_line(section['display_informations']['code']).set_description(
                "to " + section['display_informations']['direction'])


# create edges from navitia api
def create_edges_from_navitia(response, graph):
    journey = response['journeys'][0]
    edges = []

    # add edges
    for section in journey["sections"]:
        # like with nodes, we do not take care of waiting sections. Transfer sections are treated after
        if section['type'] != "waiting" and section['type'] != "transfer":
            src = calculate_node_coord_from_navitia(section['from'])
            dest = calculate_node_coord_from_navitia(section['to'])
            # we verify that both of the nodes are in the graph
            if graph.find_node_from_coord(src.coord) and graph.find_node_from_coord(dest.coord):
                # adding the edge to the node
                edge = Edge(graph.find_node_from_coord(src.coord), graph.find_node_from_coord(dest.coord),
                            section['duration'], section['duration'])
                set_edge_info(section, edge)
                edges.append(edge)
            # todo add else -> throw error
        # if the section is of type transfer, we only verify that source and destination are different to add the edge to the graph
        elif section['type'] == "transfer":
            if section['from']['name'] != section['to']['name']:
                src = calculate_node_coord_from_navitia(section['from'])
                dest = calculate_node_coord_from_navitia(section['to'])
                if graph.find_node_from_coord(src.coord) and graph.find_node_from_coord(dest.coord):
                    edge = Edge(graph.find_node_from_coord(src.coord), graph.find_node_from_coord(dest.coord),
                                section['duration'],
                                section['duration'])
                    set_edge_info(section, edge)
                    edges.append(edge)
    return edges
