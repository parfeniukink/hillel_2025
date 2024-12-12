# Example with prices

```python
"""
package
    module (file)
        class Price
            foo()
            convert
"""

class Price:
    def __init__(self, value: int, currency: str):
        self.value: int = value
        self.currency: str = currency

    @staticmethod
    def foo(...):
        pass

    def convert(self, to: str) -> "Price": ...


price = Price(value=100, currency="usd")
print(price.convert)

Price.foo()
price.foo()
# Price.foo(price)
```

# MRO detailed
