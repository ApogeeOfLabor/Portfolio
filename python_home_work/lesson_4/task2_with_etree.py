def currency_rates(url, name_valute):
    response = requests.get(url)
    data = response.text

    dom_data_valute = ET.fromstring(data)

    for inner_item in dom_data_valute.findall('Valute'):
        char_valute = inner_item.find('CharCode').text
        value_valute = inner_item.find('Value').text

        if char_valute.lower() == name_valute.lower():
            return '.'.join(value_valute.split(','))


if __name__ == '__main__':
    import requests
    import xml.etree.ElementTree as ET

    url = 'http://www.cbr.ru/scripts/XML_daily.asp'

    print(currency_rates(url, 'eur'), sep='\n')



