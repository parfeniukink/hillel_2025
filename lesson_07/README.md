# Compound statements

## `match/case`

```python
"""
match expression:
    case pattern_1:
        ...
    case pattern_2:
        ...
    case _:
        ...
"""

def check_http_status(status_code: int):
    if status_code == 200:
        print("OK")
    elif status_code == 400:
        print("Bad request")
    elif status_code == 500:
        print("Internal server error")
    else:
        print("Unrecognized status code")


or
def check_http_status(self, status_code: int):
    match status_code:
        case 200:
            print("OK")
        case 400:
            print("Bad request")
        case 500:
            print("Internal server error")
        case _:
            print("Unrecognized status code")
check_http_status(220)


def process_coordinates(coordinates: tuple[int, int]) -> str:
    match coordinates:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"On x it is {x}"
        case (0, y):
            return f"On y it is {y}"
        case (x, y):
            return f"On x,y it is ({x},{y})"
        case _:
            return "unrecognized"


print(process_coordinates(coordinates=(0, 0)))
print(process_coordinates(coordinates=(13, 0)))
print(process_coordinates(coordinates=(0, 15)))
print(process_coordinates(coordinates=(13, 15)))


x = 10

match x:
    case 10:
        print("Matched 10")
    case y:  # not recognized
        print(f"Matched {x}")
    case _:
        print("unrecognized")
```

## exceptions

```python
"""
try/except/else/finally
"""

import random

# try:
#     result = check()
#     # result.action()
# except Exception as error:
#     log(...)
# else:
#     result.action()
# finally:
#     ...


def baz() -> str:
    if random.random() > 0.5:
        raise ValueError()
    else:
        return "baz"


def bar() -> str:
    value: str = baz()
    return value


def foo():
    value: str = bar()
    return value


def main():
    try:
        result: str = foo()
    except ValueError as error:
        print(f"Value error catcehd: {error}")
    except TypeError as error:
        print(f"Type error catcehd: {error}")
    except Exception as error:
        print(f"Exception catcehd: {error}")
    else:
        print(f"Result is {result}")


main()
```

## with Saver example

```python
"""
with expression as variable:
    ...
"""

from collections.abc import Callable
from pathlib import Path
from typing import Any


def save_to_file(filename: str):
    def wrapper(func: Callable):
        def inner():
            data = func()

            with open(filename, "w") as file:
                file.write("\n".join(data))

            print(f"data is saved to the file: {filename}")

        return inner

    return wrapper


class Saver:
    def __init__(self, filename: str) -> None:
        self._filename: str = filename
        self._file_proxy = Path(filename)
        self._file = None

    def __enter__(self):
        if not self._file_proxy.exists():
            raise ValueError(f"File {self._filename} not exists")
        self._file = open(self._file_proxy, "w")
        return self

    def __exit__(self, *args, **kwargs):
        if self._file is None:
            raise ValueError("No file is opened...")
        else:
            self._file.close()

    def save(self, data: Any):
        if self._file is None:
            raise ValueError("No file is opened...")
        else:
            if isinstance(data, list):
                self._file.write("\n".join(data))
            else:
                raise ValueError("only list of strings is available")


def ask_user_input() -> list:
    results: list[str] = []
    while user_input := input("Enter next token: "):
        results.append(user_input)

    return results


def main():
    with Saver(filename="inputs.txt") as saver:
        saver.save(ask_user_input())

    with Saver(filename="prompts.txt") as saver:
        saver.save(ask_user_input())


main()
```

## BigFileReader context manager
```python
from collections.abc import Callable
from pathlib import Path
from typing import Any


class BigFileReader:
    def __init__(self, filename: str) -> None:
        self.filename: str = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename)
        return self

    def __exit__(self, *args, **kwargs):
        if self.file:
            self.file.close()

    def next_line(self):
        if not self.file:
            raise ValueError(
                f"There is no file {self.filename}",
            )
        return self.file.readline()

    def lines(self):
        pass

    def safe_read(self):
        if not self.file:
            raise ValueError(
                f"There is no file {self.filename}",
            )

        while True:
            if line := self.file.readline():
                if "john" in line:
                    print("continue")
                    continue
                else:
                    return line

    def safe_read_all(self):
        if not self.file:
            raise ValueError(
                f"There is no file {self.filename}",
            )

        else:
            while True:
                if line := self.file.readline():
                    if "john" in line:
                        continue
                    else:
                        yield line
                else:
                    break


with BigFileReader("big.txt") as reader:
    for line in reader.safe_read_all():
        ...
```
