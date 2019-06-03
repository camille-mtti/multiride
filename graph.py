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

    def find_edge(self, src, dest):
        for e in self.edges:
            if e.src == src and e.dest == dest:
                return e
        return None

    def find_min_edge(self, src, dest):
        edge = self.find_edge(src, dest)
        for e in self.edges:
            if e.src == src and e.dest == dest:
                if(e < edge):
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
                print(n.src.address + "  " + n.dest.address + " " + n.type + " " + str(n.price))
            else:
                print(n.src.address + "  " + n.dest.address + " " + n.type)

    def min_distance(self, Q, dist):
        min = sys.maxsize
        for node in Q:
            if dist[self.nodes.index(node)] < min:
                min = dist[self.nodes.index(node)]
                min_index = self.nodes.index(node)
        # todo : what to do when if is not respected
        return self.nodes[min_index]

    def dijkstra(self, source, target):
        dist = []
        path = {}
        Q = []
        final_list = []

        print("dijkstra begins")
        # init distances
        for node in self.nodes:
            dist.append(sys.maxsize)
            Q.append(node)
        dist[self.nodes.index(source)] = 0

        while Q:
            u = self.min_distance(Q, dist)
            Q.remove(u)

            # todo verify here there are problems : edge not found
            for node in u.neighbours:
                edge = self.find_min_edge(u, node)
                if dist[self.nodes.index(node)] > dist[self.nodes.index(u)] + edge.weight:
                    dist[self.nodes.index(node)] = dist[self.nodes.index(u)] + edge.weight
                    path[self.nodes.index(node)] = edge

        for key, value in path.items():
            print(key)
            print(value.src.address + " - " + value.dest.address)

        # n = target
        # while n != source:
        #     final_list.append(n)
        #     n = path[self.nodes.index(n)]
        # final_list.append(n)

        # for node in final_list:
        #     print(node.address)
        # return final_list
