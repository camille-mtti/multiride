class Edge:
  def __init__(self, src, dest, weight, duration):
    self.src = src
    self.dest = dest
    self.weight = weight
    self.type = None
    self.avoidedEdges = []
    self.line = None
    self.duration = duration
    self.price = None
    self.description = None


  def addAvoidedEdge(self, edge):
    self.avoidedEdges.append(edge)

  def setPrice(self, price):
    self.price = price
    return self

  def setDescription(self, desc):
    self.description = desc
    return self

  def setLine(self, line):
    self.line = line
    return self

  def setType(self,type):
    self.type = type
    return self
