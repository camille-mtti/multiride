import requests
import json




def get_navitia_journey(source, dest):
    r = requests.get('https://api.navitia.io/v1/coverage/fr-idf/journeys?from=' + source + '&to=' + dest,
                     auth=('be72cc2c-e6eb-4628-9a88-b7c54746c61a', ''))
    response = json.loads(r.text)
    return response


print(get_navitia_journey("2.304648;48.834698", "2.295508;48.8744088")['journeys'][0]['sections'][1]['display_informations'])

#{"lattitude": "48.834698","longitude": "2.304648"}
#{"lattitude":"48.8744088","longitude":"2.295508"}

