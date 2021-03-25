import requests
import json

response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
result_dict = json.loads(response.content)

def currency_rates(curr):
    curr = curr.upper()
    if curr in result_dict['Valute']:
        result = result_dict['Valute'][curr]['Value']
        print(float(result))
    else:
        print('None')

