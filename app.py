from flask import Flask
from flask import request
from flask import jsonify
import journey
import coordinate
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


@app.route('/geocode', methods=['POST'])
def get_geocode():
    content = request.data
    content = json.loads(content)["address"]
    coord = coordinate.get_coordinates(content)
    return jsonify(lattitude=coord[0], longitude=coord[1])


@app.route('/journey',methods=['POST'])
def get_journey():

    #loads content from request body
    content = request.data
    source = json.loads(content)["from"]
    destination = json.loads(content)["to"]

    #geocode coordinates
    source_coord = coordinate.get_coordinates(source)
    source_coord = coordinate.get_coordinates_string(source_coord)
    print(source_coord)
    #transform into string
    dest_coord = coordinate.get_coordinates(destination)
    dest_coord = coordinate.get_coordinates_string(dest_coord)

    #request for journey
    transport = journey.get_navitia_journey(source_coord, dest_coord)
    return jsonify(transport)

