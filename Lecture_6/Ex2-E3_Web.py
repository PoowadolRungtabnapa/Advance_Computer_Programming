import requests

url = 'https://th.wikipedia.org/wiki/รายชื่อเทศบาลตำบลในประเทศไทย'
resp = requests.get(url)
print(resp)
print(resp.text[:5_000])