import bs4
import requests
response = requests.get('https://www.borntodev.com/blog/')
page_data = bs4.BeautifulSoup(response.text, 'html.parser')
data_list = page_data.find_all("div", class_="post-header")
'''print(data_list)'''
for i in data_list:
    data = i
    print(data[10:])
