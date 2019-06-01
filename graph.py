from node import Node
from edge import Edge
import coordinate


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def print_nodes(self):
        print('mes nodes : ')
        for n in self.nodes:
            print(n.coord + "  " + n.address)

    def find_node_from_coord(self,coord):
        for node in self.nodes:
            if (node.coord == coord) :
                return node
        return None

    def add_nodes(self,ns):
        for n in ns:
            self.nodes.append(n)

    def add_edges(self,es):
        for e in es :
            self.edges.append(e)

    def find_edge(self, src, dest):
        for e in self.edges :
            if e.src == src and e.dest == dest:
                return e
        return None

    def print_edges(self):
        print('mes edges : ')
        for n in self.edges:
            if(n.price):
                print(n.src.address + "  " + n.dest.address + " " + n.type+" "+str(n.price))
            else:
                print(n.src.address + "  " + n.dest.address + " " + n.type)





