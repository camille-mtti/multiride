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
        # we calculate every uber traject between every node of our graph
        for i in range(0, len(graph.nodes) - 1):
            src = graph.nodes[i]
            for j in range(i + 1, len(graph.nodes)):
                dest = graph.nodes[j]
                graph_edge = graph.find_edge(graph.nodes[i], graph.nodes[j])
                # we skip taking a uber if the edge is less than 10 min walking
                if graph_edge and graph_edge.type == "walking" and graph_edge.duration < 6000:
                    print("skipping uber edge" + graph_edge.src.address + " " + graph_edge.dest.address)
                else:
                    # we call the uber api to have information
                    result = self.estimate_traject(src.coord, dest.coord)
                    # if the price is in our budget we add the edge to the graph
                    if result.time > 10 and result.price < price:
                        this_edge = Edge(src, dest, result.time * 0.5, result.time)
                        this_edge.set_type("Uber").set_price(result.price).set_description(
                            "Uber journey, available on the Uber App for more info")
                        edges.append(this_edge)
        return edges
