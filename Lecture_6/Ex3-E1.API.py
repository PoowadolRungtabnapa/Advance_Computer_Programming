import requests
response = requests.get('https://api.exchangeratesapi.io/latest?base=THB')
exchange_rates = eval(response.text)["rates"]
my_money = int(input('Enter Your Money : '))
exchange = input('Enter Your Exchange Money : ').upper()
print(exchange_rates[exchange]*my_money)
