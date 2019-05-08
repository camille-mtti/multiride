import requests
import json


# get coordinates of an address
def get_coordinates(address):
    #https://nominatim.openstreetmap.org/search?<params>
    r = requests.get('https://nominatim.openstreetmap.org/search?format=json&q=' + address)
    response = json.loads(r.text)
    lat = response[0]['lat']
    lon = response[0]['lon']
    return [lat, lon]


def get_navitia_journey(source,dest):
    r = requests.get('https://api.navitia.io/v1/coverage/sandbox/journeys?from=' + source + '&to=' + dest,
                     auth=('be72cc2c-e6eb-4628-9a88-b7c54746c61a', ''))
    response = json.loads(r.text)
    return response


print(get_navitia_journey("48,834698,2.304648", "48.8744088,2.295508"))

#{"lattitude": "48.834698","longitude": "2.304648"}
#{"lattitude":"48.8744088","longitude":"2.295508"}

