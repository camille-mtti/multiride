from flask import Flask
from flask import request
from flask import jsonify
import journey
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
    coord = journey.get_coordinates(content)
    return jsonify(lattitude=coord[0], longitude=coord[1])

@app.route('/journey',methods=['POST'])
def get_journey():


