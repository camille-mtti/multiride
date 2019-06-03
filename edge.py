class Edge:
  def __init__(self, src, dest, type, weight, duration):
    self.src = src
    self.dest = dest
    self.weight = weight
    self.type = type
    self.avoidedEdges = []
    self.line = None
    self.duration = duration
    self.price
    self.description

    # Add neighbour
    self.src.neighbours.append(self.dest);


  def addAvoidedEdge(self, edge):
    self.avoidedEdges.append(edge)
    