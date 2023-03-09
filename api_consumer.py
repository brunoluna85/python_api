import requests
import json

def prettify(ugly_json):
    return json.dumps(ugly_json, indent=4)

REQUEST = 'http://localhost:5001/characters'

response = requests.get(REQUEST)
response_json = response.json()

print(prettify(response_json))

#for character in response.json()['characters']:
#    print(character)

