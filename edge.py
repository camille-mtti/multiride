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

        # Add neighbour
        self.src.neighbours.append(self.dest);

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

    def setType(self, type):
        self.type = type
        return self

    def __lt__(self, other):
        return self.weight<other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __gt__(self, other):
        return self.weight >= other.weight

    def __ge__(self, other):
        return self.weight > other.weight
