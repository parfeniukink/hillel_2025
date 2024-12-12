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

# Methods

## 1. String (str) Methods:

`str.upper()`: Converts all characters to uppercase.
`str.lower()`: Converts all characters to lowercase.
`str.capitalize()`: Capitalizes the first character.
`str.title()`: Converts the string to title case.
`str.strip()`: Removes leading and trailing whitespace.
`str.lstrip()`: Removes leading whitespace.
`str.rstrip()`: Removes trailing whitespace.
`str.replace(old, new)`: Replaces all occurrences of old with new.
`str.split(separator)`: Splits the string into a list based on the separator.
`str.join(iterable)`: Joins elements of an iterable with the string.
`str.startswith(prefix)`: Returns True if the string starts with the given prefix.
`str.endswith(suffix)`: Returns True if the string ends with the given suffix.
`str.find(substring)`: Returns the lowest index of the substring, or -1 if not found.
`str.index(substring)`: Like find() but raises a ValueError if not found.
`str.isalpha()`: Returns True if all characters are alphabetic.
`str.isdigit()`: Returns True if all characters are digits.
`str.isalnum()`: Returns True if all characters are alphanumeric.
`str.isspace()`: Returns True if all characters are whitespace.
`str.count(substring)`: Returns the number of non-overlapping occurrences of the substring.

## 2. List (list) Methods:

`list.append(item)`: Adds item to the end of the list.
`list.insert(index, item)`: Inserts item at the specified index.
`list.remove(item)`: Removes the first occurrence of item.
`list.pop([index])`: Removes and returns the item at index, or the last item if index is not specified.
`list.clear()`: Removes all items from the list.
`list.index(item)`: Returns the index of the first occurrence of item.
`list.count(item)`: Returns the number of occurrences of item.
`list.sort()`: Sorts the list in ascending order.
`list.reverse()`: Reverses the list in place.
`list.extend(iterable)`: Extends the list by appending elements from an iterable.

## 3. Dictionary (dict) Methods:

`dict.get(key, default=None)`: Returns the value for key if it exists, otherwise returns default.
`dict.keys()`: Returns a view object with all the dictionary's keys.
`dict.values()`: Returns a view object with all the dictionary's values.
`dict.items()`: Returns a view object with the dictionary’s key-value pairs.
`dict.update(other_dict)`: Updates the dictionary with another dictionary's key-value pairs.
`dict.pop(key)`: Removes the key and returns its value, or raises a KeyError.
`dict.popitem()`: Removes and returns the last inserted key-value pair.
`dict.clear()`: Removes all items from the dictionary.
`dict.setdefault(key, default=None)`: Returns the value if the key exists, otherwise inserts the key with the default value.

## 4. Tuple (tuple) Methods:

`tuple.count(item)`: Returns the number of occurrences of item.
`tuple.index(item)`: Returns the index of the first occurrence of item.

## 5. Set (set) Methods:

`set.add(item)`: Adds item to the set.
`set.remove(item)`: Removes item from the set, raises a KeyError if not found.
`set.discard(item)`: Removes item from the set if it is present, does nothing if not found.
`set.pop()`: Removes and returns an arbitrary element from the set.
`set.clear()`: Removes all elements from the set.
`set.union(other_set)`: Returns the union of sets.
`set.intersection(other_set)`: Returns the intersection of sets.
`set.difference(other_set)`: Returns the difference of sets.
`set.symmetric_difference(other_set)`: Returns the symmetric difference of sets.
`set.update(other_set)`: Updates the set with the union of sets.
`set.intersection_update(other_set)`: Updates the set with the intersection.
`set.difference_update(other_set)`: Updates the set with the difference.
`set.symmetric_difference_update(other_set)`: Updates the set with the symmetric difference.

## 6. Integer (int) Methods:

`int.bit_length()`: Returns the number of bits required to represent the integer in binary.
`int.to_bytes(length, byteorder)`: Returns an array of bytes representing the integer.
`int.from_bytes(bytes, byteorder)`: Converts a byte array back into an integer.
`int.__add__()`, int.**sub**(), etc.: Magic methods for arithmetic operations like addition, subtraction, etc.

## 7. Float (float) Methods:

`float.is_integer()`: Returns True if the float is an integer (e.g., 3.0).
`float.as_integer_ratio()`: Returns a tuple of integers representing the float as a ratio.
`float.hex()`: Returns a hexadecimal representation of the float.
`float.fromhex(string)`: Converts a hexadecimal string to a float.

## 8. Boolean (bool) Methods:

`bool.__and__(other)`: Logical AND operation.
`bool.__or__(other)`: Logical OR operation.
`bool.__xor__(other)`: Logical XOR operation.

## MRO example with Facilities

```python
import random
import string


class Product:
    def __init__(self, name: str, price: int) -> None:
        self.name: str = name
        self.price: int = price

    def __str__(self) -> str:
        return f"{self.name}: {self.price}$"


class Factory:
    def build(self) -> Product:
        # "".join(['a', 'e', 'w', 'q', ...]) => aewq
        random_name: str = "".join(
            [random.choice(string.ascii_letters) for i in range(10)]
        )
        random_price: int = random.randint(10, 20)
        return Product(name=random_name, price=random_price)


class PdfGenerator:
    def generate_pdf(self, filename):
        print(f"Generating PDF: {filename}.pdf")

    def create_order_documnet(self):
        print("Stub")


class Legals(PdfGenerator):
    def create_order_documnet(self):
        self.generate_pdf(filename="legals")
        super().create_order_documnet()


class Delivery(PdfGenerator):
    def ship(self, product: Product):
        print(f"Shipping the product: {product.name}")

    def create_order_documnet(self):
        self.generate_pdf(filename="delivery")
        super().create_order_documnet()


class TeslaFacility(Factory, Delivery, Legals):
    def create_order_documnet(self):
        return super().create_order_documnet()


class IntelFacility(Factory, Legals, Delivery):
    pass


tesla_in_kyiv = TeslaFacility()
tesla_in_california = TeslaFacility()

intel_in_kyiv = IntelFacility()
intel_in_california = IntelFacility()


tesla_model_x: Product = tesla_in_california.build()
tesla_in_california.create_order_documnet()
# print(TeslaFacility.__mro__)
```
