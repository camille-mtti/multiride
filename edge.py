class Edge:
    def __init__(self, src, dest, weight, duration):
        self.src = src
        self.dest = dest
        self.weight = weight
        self.type = None
        self.line = None
        self.duration = duration
        self.price = None
        self.description = None
        # add neighbours for the nodes
        # it is a directed graph so only the src node has dest as neighbour
        self.src.neighbours.append(self.dest)

    # methods to add caracteristics to edge to avoid to have a gigantic constructor
    # the methods can be called successively

    def set_price(self, price):
        self.price = price
        return self

    def set_description(self, desc):
        self.description = desc
        return self

    def set_line(self, line):
        self.line = line
        return self

    def set_type(self, type):
        self.type = type
        return self

    # Comparable for edges (regarding their weight)
    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __gt__(self, other):
        return self.weight >= other.weight

    def __ge__(self, other):
        return self.weight > other.weight
