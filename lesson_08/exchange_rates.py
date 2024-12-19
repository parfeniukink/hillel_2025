"""
Exchange rates implementation


ExchangeRates:
    - origin
    - currencies
    - convert()
"""

import time


Currencies = dict[str, dict[str, float]]


def get_exchnage_rates_from_internet() -> Currencies:
    time.sleep(2)
    return {
        "usd": {
            "uah": 0.02380952,
            "chf": 1.2,
        },
        "uah": {
            "usd": 42,
            "chf": 50,
        },
    }


class CurrencyNotFoundError(Exception):
    pass


class ExchangeRates:
    print("Hello")

    while True:
        print("...")

    def __init__(self) -> None:
        self._data: Currencies = get_exchnage_rates_from_internet()

    def convert(self, value: float, from_: str, to: str) -> float:
        try:
            coef: float = self._data[from_][to]
        except KeyError as error:
            raise CurrencyNotFoundError("Currency not found") from error

        result = value * coef
        return result


def first_calculation(service: ExchangeRates):
    price: float = 100.0  # uah

    try:
        converted: float = service.convert(price, from_="uah", to="usd")
    except CurrencyNotFoundError as error:
        print(error)
    else:
        print(f"Converted value is {converted}")


def second_calculation(service: ExchangeRates):
    price: float = 50.0  # usd

    try:
        converted: float = service.convert(price, from_="usd", to="uah")
    except CurrencyNotFoundError as error:
        print(error)
    else:
        print(f"Converted value is {converted}")


def main():
    print("Application started")
    service = ExchangeRates()
    first_calculation(service)
    second_calculation(service)


main()
