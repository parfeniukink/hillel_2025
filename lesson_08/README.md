# Concurrency

- CPU-bound
- IO-bound

# Base asyncio example

```python
import time
import asyncio


async def foo():
    print("started foo")
    await asyncio.sleep(2)
    print("finished foo")


async def bar():
    print("started bar")
    await asyncio.sleep(2)
    print("finished bar")


async def main():
    await asyncio.gather(foo(), bar())



start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()
print(f"Execution time: {end - start}")
```

# Async Generator

```python
import time
import asyncio


async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        yield i


async def main():
    async for item in async_generator():
        print(item)



asyncio.run(main())
```

# Async Context Manager

```python
import asyncio


class AsyncFile:
    async def __aenter__(self):
        print("Opening file")
        await asyncio.sleep(1)
        print("File opened")
        return self

    async def __aexit__(self, *args, **kwargs):
        print("Closing file")
        await asyncio.sleep(1)
        print("File closed")


async def main():
    async with AsyncFile():
        print("Reading file ...")


asyncio.run(main())
```

# Singleton pattern

```python
class Singleton:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            print("creating")
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self) -> None:
        if Singleton._initialized is True:
            return

        print("initializing")
        Singleton._initialized = True


instance1 = Singleton()
instance2 = Singleton()

print(id(instance1))
print(id(instance2))
```

# Dependency injection

```python
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
```
