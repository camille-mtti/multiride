class Edge:
  def __init__(self, src, dest, type, weight):
    self.src = src
    self.dest = dest
    self.weight = weight
    self.type = type
    self.avoidedEdges = []

  def addAvoidedEdge(self, edge):
    self.avoidedEdges.append(edge)
    