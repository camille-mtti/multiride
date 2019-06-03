class Node:
    def __init__(self, coord, address):
        self.neighbours = []
        self.coord = coord
        self.address = address

    # add comparable for Nodes to verify two nodes are identical
    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return self.coord == other.coord and self.address == other.address
