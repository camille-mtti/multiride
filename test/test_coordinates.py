from unittest import TestCase
import coordinate

class TestCoordinates(TestCase):

  def test_get_coordinates(self):
    coord = coordinate.get_coordinates("22 rue de Vouillé, Paris, France")
    self.assertEquals(coord, ["48.834698", "2.304648"])

  def test_false_address(self):
    with self.assertRaises(Exception):
      coordinate.get_coordinates("lorem ipsum")
