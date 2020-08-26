import requests
import json
response = requests.get('https://restcountries.eu/rest/v2/regionalbloc/asean')
for i in response :
    print(i)

