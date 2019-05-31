from node import Node
from edge import Edge
import coordinate


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def create_node_from_navitia(self, response):

        # load data from first journey from navitia
        journey = response['journeys'][0]
        temp = journey['sections'][0]['from']

        # add first node
        node = self.calculate_node_coord_from_navitia(temp)
        self.nodes.append(node)

        # add other nodes
        for section in journey["sections"]:
            if section['type'] != "waiting" and section['type'] != "transfer":
                temp = section['to']
                node = self.calculate_node_coord_from_navitia(temp)
                self.nodes.append(node)

        print('mes nodes : ')
        for n in self.nodes:
            print(n.coord + "  " + n.address)

    def find_node_from_coord(self,coord):
        for node in self.nodes:
            if (node.coord == coord) :
                return node
        return None

    def calculate_node_coord_from_navitia(self, src):
        if src['embedded_type'] == "address":
            node = Node(src['id'], src['name'])
        elif src['embedded_type'] == "stop_point":
            coord = coordinate.get_coordinates_string(coordinate.get_coordinates(src['name']))
            node = Node(coord, src['name'])
        return node

    def calculate_section_type(self,section):
        if(section['type']=="street_network"):
            if (section['mode']=='walking'):
                return "walking"
        if(section['type']=="public_transport"):
            return "metro"

    def create_edges_from_navitia(self, response):
        journey = response['journeys'][0]


        # add edges

        for section in journey["sections"]:
            if section['type'] != "waiting" and section['type'] != "transfer":

                src = self.calculate_node_coord_from_navitia(section['from'])
                dest = self.calculate_node_coord_from_navitia(section['to'])
                if self.find_node_from_coord(src.coord) and self.find_node_from_coord(dest.coord):
                        edge = Edge(self.find_node_from_coord(src.coord),self.find_node_from_coord(dest.coord),self.calculate_section_type(section),1)
                        self.edges.append(edge)
        print('mes edges : ')
        for n in self.edges:
            print(n.src.address + "  " + n.dest.address + " " + n.type)





