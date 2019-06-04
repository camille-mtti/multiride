from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
import journey
import coordinate
import json

from os import getenv

app = Flask(__name__)


# test git config n2
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/geocode', methods=['POST'])
def get_geocode():
    content = request.data
    content = json.loads(content)["address"]
    coord = coordinate.get_coordinates(content)
    return jsonify(lattitude=coord[0], longitude=coord[1])


@app.route('/journey', methods=['POST'])
def get_journey():
    # loads content from request body
    content = request.data
    source = json.loads(content)["from"]
    destination = json.loads(content)["to"]
    price = json.loads(content)["price"]

    # geocode coordinates
    source_coord = coordinate.get_coordinates(source)
    source_coord = coordinate.get_coordinates_string(source_coord)

    dest_coord = coordinate.get_coordinates(destination)
    dest_coord = coordinate.get_coordinates_string(dest_coord)

    # request for journey
    transport = journey.get_journey(source_coord, dest_coord, price)
    response = []
    for e in reversed(transport):
        response.append({
            "from": e.src.address, "to": e.dest.address, "type": e.type, "line": e.line, "cost": e.price,
            "description ": e.description, "duration": e.duration})
    return Response(json.dumps(response), mimetype="application/json")


if __name__ == '__main__':
    app.run()
