# Homework

### Create a class `Price` _(for more details look at lesson)_

- Acceptance criteria:

  - IF I create 2 instances of a `Price` I want to perform next operations on them:
    - ADDING prices with the same currency
    - doing a SUBTRACTION of prices with the same currency

- Additional (optional): _operations between prices with different currencies_:
  - IF price instances' CURRENCIES are DIFFERENT I want to apply a "MIDDLE" CONVERSION
    - "CHF" is a middle currency. The conversion logic is below
  - The RESULTING PRICE must have a CURRENCY of the price that is on the LEFT (`self`)

The pseudo code that explains how the logic works:

```python
class Price(NamedTuple):
    value: int
    currency: str

a = Price(100, "USD")
b = Price(100, "USD")

a + b == (a.convert(to="CHF") + b.convert(to="CHF").convert(to=a.currency)
```

```python
class Price:
	def __init__(self, value: int, currency: str) -> None:
		self.value: int = value
		self.currency: str = currency

    # TODO: complete the class
```

### Authorization decorator (optional)

About the project below:

- `users` list includes multiple users (define them by yourself)
- `command()` is only a single function that mimics the business logic
- `auth()` is a decorator that requires user authorization to perform tasks

What I need from you?

- I need you to complete the `auth()` decorator. other code changes are also available but not required
- if the function is decorated with `auth` - the application ASKS user for `username` and `password`
- ASK credentials UNTIL they are CORRECT
- IF credentials are CORRECT - EXECUTE the command
- IF User has entered credentials CORRECTLY once - it is CACHED and used to call future commands WITHOUT additional AUTHORIZATION
