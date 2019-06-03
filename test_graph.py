from unittest import TestCase
from node import Node
from edge import Edge
from array import array
import coordinate
import sys
from graph import Graph


class TestGraph(TestCase):
    graph = Graph()
    nodes = [Node("2 rue de vouillé 75015", "2.304648;48.834698"),
             Node("28 rue notre dame des champs, 75015 Paris france", "2.328013;48.845315")]

    def test_add_nodes(self):
        self.graph.add_nodes(self.nodes)
        self.assertEqual(len(self.graph.nodes), 2)

    def test_add_edges(self):
        edges = [Edge(self.nodes[0], self.nodes[1], 1, 100)]
        self.graph.add_edges(edges)
        self.assertEqual(len(self.graph.edges), 1)

    def test_find_node(self):
        self.assertEqual(self.graph.find_node(self.nodes[0]), self.nodes[0])
        self.assertEqual(self.graph.find_node_from_coord(self.nodes[0].coord),self.nodes[0])
