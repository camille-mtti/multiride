from os import getenv
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from dotenv import load_dotenv
import json
load_dotenv()

class Uber:
  # Init the uber session and client
  def __init__(self):
    self.session = Session(server_token=getenv('SERVER_TOKEN'))
    self.client = UberRidesClient(self.session)

  def estimate_time(self, start_coord, end_coord):
    # Get prices and time estimates
    estimates = self.client.get_price_estimates(
      start_latitude=start_coord.split(";")[1],
      start_longitude=start_coord.split(";")[0],
      end_latitude=end_coord.split(";")[1],
      end_longitude=end_coord.split(";")[0],
      seat_count=2
    )

    print(json.dumps(estimates.json.get("prices"), indent=2))
    
    # Search for UberX and return the average price and the time in a dict
    for estimate in estimates.json.get("prices"):
      if estimate["localized_display_name"] == "UberX":
        return {
          "price": (estimate["high_estimate"] + estimate["low_estimate"]) / 2,
          "time": estimate["duration"]
        }
