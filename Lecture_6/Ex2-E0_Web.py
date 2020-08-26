import bs4
import requests
response = requests.get('https://www.borntodev.com/blog/')
page_data = bs4.BeautifulSoup(response.text, 'html.parser')
print(page_data.prettify())