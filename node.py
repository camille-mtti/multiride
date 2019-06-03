class Node:
  def __init__(self, coord, address):
    self.neighbours = []
    self.coord = coord
    self.address = address

  def __eq__(self, other):
    if not isinstance(other, Node):
      # don't attempt to compare against unrelated types
      return NotImplemented

    return self.coord == other.coord and self.address == other.address
