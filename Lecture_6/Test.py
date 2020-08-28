import requests
response = requests.get('https://restcountries.eu/rest/v2/regionalbloc/asean')
print(response.json())
