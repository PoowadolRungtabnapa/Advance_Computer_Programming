import requests

BASE = 'http://127.0.0.1:5000/'

responses = requests.get(BASE + 'product')

print(responses.json())
