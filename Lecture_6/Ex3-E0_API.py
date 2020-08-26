import requests
response = requests.get('https://api.exchangeratesapi.io/latest?base=THB')
print(response.text)