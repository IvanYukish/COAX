import requests, json


def poloniex():
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    api = requests.get(url)
    data = json.loads(api.text)
    return data


def EUR_to_USD():
    polo = poloniex()
    for i in polo[1]:
        print(i)


def UAH_to_USD():
    polo = poloniex()
    for i in polo[0]:
        print(i[3])


def main():
    polo = poloniex()
    for k in polo:
        # if k.get('ccy')
        print(k)


if __name__ == '__main__':
    main()
