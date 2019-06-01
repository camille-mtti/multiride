from os import getenv
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from dotenv import load_dotenv
import json
from edge import Edge

load_dotenv()


class Uber:
    # Init the uber session and client
    def __init__(self):
        self.session = Session(server_token=getenv('SERVER_TOKEN'))
        self.client = UberRidesClient(self.session)
        self.price = 0
        self.time = 0

    def estimate_traject(self, start_coord, end_coord):

        # Get prices and time estimates
        estimates = self.client.get_price_estimates(
            start_latitude=start_coord.split(";")[1],
            start_longitude=start_coord.split(";")[0],
            end_latitude=end_coord.split(";")[1],
            end_longitude=end_coord.split(";")[0],
            seat_count=2
        )

        # Search for UberX and return the average price and the time in a dict
        for estimate in estimates.json.get("prices"):
            if estimate["localized_display_name"] == "UberX":
                self.price = (estimate["high_estimate"] + estimate["low_estimate"]) / 2
                self.time = estimate["duration"]
                return self

    def create_uber_trajects(self, graph, price):
        edges = []
        for i in range(0,len(graph.nodes)-1):
            src = graph.nodes[i]
            for j in range(i, len(graph.nodes)-1):
                dest = graph.nodes[j]
                graph_edge = graph.find_edge(i,j)
                if graph_edge and graph_edge.type == "walking" and graph_edge.duration < 6000 :
                    print("skipping uber edge" + graph_edge.src.address + " " + graph_edge.dest.address)
                else:
                    result = self.estimate_traject(src.coord, dest.coord)

                    if result.time >10 and result.price<price:
                        this_edge = Edge(src, dest, "uber", 1, result.time)
                        edges.append(this_edge)
        return edges


'''
For i in range 0:nb_of_nodes : 
   For j in range i :nb_of_nodes :
       If (edge.duration > 600 && edge.type == walking ) :
          Edge = Uber_edge(node(i), node(j)
           If edge.price < budget_max
                 Edges.append(edge)
'''