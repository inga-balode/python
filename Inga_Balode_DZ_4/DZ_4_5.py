import sys
import requests
import json

response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
result_dict = json.loads(response.content)

i = []
def currency_rates(argv):
    i = map(str, argv)
    for curr in i:
        print(result_dict['Valute'][curr]['Value'])


if __name__ == '__main__':
    currency_rates(sys.argv[1:])
    exit(0)
