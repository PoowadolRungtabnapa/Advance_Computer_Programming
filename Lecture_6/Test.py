import requests
response = requests.get('https://restcountries.eu/rest/v2/regionalbloc/asean')
print('-'*75)
print('Country Name\t\t\t\tArea\t\t\tPopulation')
print('-'*75)
for i in response.json() :
    if len(i["name"]) <= 7 :
        print(f"{i['name']}\t\t\t\t\t{i['area']}\t\t{i['population']}")
    elif len(i["name"]) < 17 and i["area"] > 10000.0:
        print(f"{i['name']}\t\t\t\t{i['area']}\t\t{i['population']}")
    elif len(i["name"]) == 17 :
        print(f"{i['name']}\t\t\t{i['area']}\t\t\t{i['population']}")
    elif i["area"] < 10000.0 :
        print(f"{i['name']}\t\t\t\t{i['area']}\t\t\t{i['population']}")
    else :
        print(f"{i['name']}\t{i['area']}\t\t{i['population']}")