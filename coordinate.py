import requests
import json

# get coordinates of an address


def get_coordinates(address):

    # https://nominatim.openstreetmap.org/search?<params>

    r = requests.get('https://nominatim.openstreetmap.org/search?format=json&q=' + address)
    response = json.loads(r.text)
    lat = response[0]['lat']
    lon = response[0]['lon']
    return [lat, lon]


def get_coordinates_string(array):
    return array[1]+";"+array[0]

