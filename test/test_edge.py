from unittest import TestCase
from node import Node
from edge import Edge

class TestEdge(TestCase):
  src = Node("2 rue de vouillé 75015", "2.304648;48.834698")
  dest = Node("28 rue notre dame des champs, 75015 Paris france", "2.328013;48.845315")

  src2 = Node("2 rue de vouillé 75015", "2.304648;48.834698")
  dest2 = Node("28 rue notre dame des champs, 75015 Paris france", "2.328013;48.845315")

  edge = Edge(src, dest, 10, 60)
  edge2 = Edge(src2, dest2, 20, 120)

  def test_set_price(self):
    self.edge.set_price(10)
    self.assertEqual(10, self.edge.price)

  def test_set_description(self):
    self.edge.set_description("This is a description")
    self.assertEqual("This is a description", self.edge.description)

  def test_set_line(self):
    self.edge.set_line(12)
    self.assertEqual(12, self.edge.line)

  def test_set_type(self):
    self.edge.set_type("uber")
    self.assertEqual("uber", self.edge.type)

  def test_lt(self):
    self.assertTrue(self.edge < self.edge2)

  def test_le(self):
    self.assertTrue(self.edge <= self.edge2)

  def test_gt(self):
    self.assertTrue(self.edge2 >= self.edge)

  def test_gt(self):
    self.assertTrue(self.edge2 > self.edge)
  