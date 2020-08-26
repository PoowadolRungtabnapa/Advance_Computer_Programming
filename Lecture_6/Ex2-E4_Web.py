import requests
import lxml.etree

url = "https://th.wikipedia.org/wiki/รายชื่อเทศบาลตำบลในประเทศไทย"
resp = requests.get(url)

content = resp.content
tree = lxml.etree.fromstring(content, parser=lxml.etree.HTMLParser())

xpath = '//*[@id="mw-content-text"]/div/table[2 <= position()]/tbody/tr/td[2 <= position() and position() <= 3]//a//text()'
tambon_list = tree.xpath(xpath)
for t_name in tambon_list :
    print(t_name)