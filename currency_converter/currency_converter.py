from decimal import *
import requests
import bs4


CB_URL = 'https://www.cbr.ru/scripts/XML_daily.asp?'


class EmptyExchangeRates(Exception):
    def __init__(self):
        self.message = 'Error while fetching data from the Central Bank API'

    def __str__(self):
        return self.message


class WrongCurrency(EmptyExchangeRates):
    def __init__(self, key):
        self.key = key
        self.message = f"There is no such currency [{self.key}] in the Central Bank exchange rates\n" \
                       f"List of currencies:\n" \
                       f"'AUD', 'AZN', 'GBP', 'AMD', 'BYN',\n" \
                       f"'BGN', 'BRL', 'HUF', 'HKD', 'DKK',\n" \
                       f"'USD', 'EUR', 'INR', 'KZT', 'CAD',\n" \
                       f"'KGS', 'CNY', 'MDL', 'NOK', 'PLN',\n" \
                       f"'RON', 'XDR', 'SGD', 'TJS', 'TRY',\n" \
                       f"'TMT', 'UZS', 'UAH', 'CZK', 'SEK',\n" \
                       f"'CHF', 'ZAR', 'KRW', 'JPY'"


def convert(amount=100, cur_from='USD', cur_to='RUR', date='') -> str:
    """
        Obtaining the exchange rate for a specific date.
        Date format must be specified as dd/mm/yyyy
    """
    response = requests.get(CB_URL, {"date_req": date})

    body = bs4.BeautifulSoup(response.content, 'xml')
    currencies = body.find_all('Valute')
    if len(currencies) == 0:
        raise EmptyExchangeRates

    exchange_rates = {}

    for currency in currencies:
        temp = list(currency.descendants)
        exchange_rates[temp[3]] = Decimal(temp[-1].replace(',', '.')) / Decimal(temp[5])

    if cur_from == 'RUR':
        try:
            result = Decimal(amount) / Decimal(exchange_rates[cur_to])
            return f"For {amount} rubles you can buy {Decimal(result).quantize(Decimal('1.0000'))} {cur_to}"
        except KeyError:
            raise WrongCurrency(cur_to)

    if cur_to == 'RUR':
        try:
            result = Decimal(exchange_rates[cur_from]) * Decimal(amount)
            return f"For {amount} {cur_from} you will receive " \
                   f"{Decimal(result).quantize(Decimal('1.0000'))} rubles"
        except KeyError:
            raise WrongCurrency(cur_from)

    try:
        exchange_rates[cur_from]
    except KeyError:
        raise WrongCurrency(f'{cur_from}')

    try:
        exchange_rates[cur_to]
    except KeyError:
        raise WrongCurrency(f'{cur_to}')

    result = (Decimal(exchange_rates[cur_from]) / Decimal(exchange_rates[cur_to])) * Decimal(amount)
    return f"For {amount} {cur_from} you will receive {Decimal(result).quantize(Decimal('1.0000'))} {cur_to}"


if __name__ == '__main__':
    print(convert(100, 'USD', 'RUR'))
