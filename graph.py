from node import Node
import coordinate

class Graph :
    def __init__(self):
        self.nodes = []

    def create_node_from_navitia(self, response):
        journey = response['journeys'][0]
        temp = journey['sections'][0]['from']
        if (temp['embedded_type'] == "address"):
            node = Node(temp['id'], temp['name'])
        elif (temp['embedded_type'] == "stop_point"):
            coord = coordinate.get_coordinates_string(
                coordinate.get_coordinates(temp['name']))
            node = Node(coord, temp['name'])
        self.nodes.append(node)

        for section in journey["sections"]:
            if (section['type'] != "waiting" and section['type'] != "transfer"):
                temp = section['to']
                if (temp['embedded_type'] == "address"):
                    node = Node(temp['id'], temp['name'])
                elif (temp['embedded_type'] == "stop_point"):
                    coord = coordinate.get_coordinates_string(coordinate.get_coordinates(temp['name']))
                    node = Node(coord, temp['name'])
                self.nodes.append(node)

        print('mes nodes : ')
        for n in self.nodes:
            print(n.coord + "  " + n.address)
