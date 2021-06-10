import requests

response = requests.get("http://api.open-notify.org/astros.json")
astro_json = response.json()
print(astro_json)


for person in astro_json['people']:
    print(person['name'])
