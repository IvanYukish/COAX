import requests
import json


def poloniex():
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    api = requests.get(url)
    data = json.loads(api.text)
    return data


def eur_to_usd(money: int) -> float:
    polo = poloniex()
    prise_eur = prise_usd = 1
    for k in polo:
        if k.get('ccy') == 'EUR':
            prise_eur = k.get('buy')
        if k.get('ccy') == 'USD':
            prise_usd = k.get('buy')
    return money * prise_eur / prise_usd


def uah_to_usd(money: int) -> float:
    polo = poloniex()
    prise_usd = 1
    for k in polo:
        if k.get('ccy') == 'USD':
            prise_usd = k.get('buy')
    return money / float(prise_usd)
