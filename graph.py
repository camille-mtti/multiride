from node import Node
from edge import Edge
from array import array
import coordinate
import sys


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def print_nodes(self):
        print('mes nodes : ')
        for n in self.nodes:
            print(n.coord + "  " + n.address)

    def find_node_from_coord(self, coord):
        for node in self.nodes:
            if (node.coord == coord):
                return node
        return None

    def add_nodes(self, ns):
        for n in ns:
            self.nodes.append(n)

    def add_edges(self, es):
        for e in es:
            self.edges.append(e)

    # simple function to return the first edge found with a source node and a destination node
    def find_edge(self, src, dest):
        for e in self.edges:
            if e.src == src and e.dest == dest:
                return e
        return None

    # function to return the edge with minimum weight of a source node and a destination node
    def find_min_edge(self, src, dest):
        edge = self.find_edge(src, dest)
        for e in self.edges:
            if e.src == src and e.dest == dest:
                if (e < edge):
                    edge = e
        return edge

    # function to return the edge with minimum weight that respect the price of a source node and a destination node
    def find_min_edge_price(self, src, dest, price, price_max):
        edge = self.find_edge(src, dest)
        for e in self.edges:
            if e.src == src and e.dest == dest:
                if (e.price):
                    p = price + e.price
                    if (e < edge and (price + e.price <= price_max)):
                        edge = e
                else:
                    if (e < edge):
                        edge = e
        return edge

    def find_node(self, node):
        for n in self.nodes:
            if n == node:
                return n
        return None

    def print_edges(self):
        print('mes edges : ')
        for n in self.edges:
            if (n.price):
                print(n.src.address + "  " + n.dest.address + " " + n.type + " " + str(n.price) + " " + str(n.duration))
            else:
                print(n.src.address + "  " + n.dest.address + " " + n.type + " " + str(n.duration))

    def min_distance(self, Q, dist):
        min = sys.maxsize
        for node in Q:
            if dist[self.nodes.index(node)] < min:
                min = dist[self.nodes.index(node)]
                min_index = self.nodes.index(node)
        # todo : what to do when if is not respected
        return self.nodes[min_index]

    def dijkstra(self, source, target, price_max):
        dist = []
        path = {}
        Q = []
        final_list = []
        price = 0

        print("-------------------- dijkstra begins ---------------------------------------------")
        # init distances
        for node in self.nodes:
            dist.append(sys.maxsize)
            Q.append(node)
        dist[self.nodes.index(source)] = 0

        while Q:
            u = self.min_distance(Q, dist)
            Q.remove(u)

            for node in u.neighbours:
                edge = self.find_min_edge_price(u, node, price, price_max)
                if dist[self.nodes.index(node)] > dist[self.nodes.index(u)] + edge.weight:
                    if edge.price:
                        price = price + edge.price
                    dist[self.nodes.index(node)] = dist[self.nodes.index(u)] + edge.weight
                    path[self.nodes.index(node)] = edge

        edge = self.dijkstra_find_dest(path, target)
        while edge.src != source:
            final_list.append(edge)
            edge = self.dijkstra_find_dest(path, edge.src)
        final_list.append(edge)

        return final_list

    def dijkstra_find_dest(self, path, target):
        for key, edge in path.items():
            if edge.dest.address == target.address:
                return edge
        return None
