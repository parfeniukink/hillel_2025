# Namespaces

## keywords

- `global`
- `nonlocal`

## builtins

```python
import builtins
print(__builtins__.__dict__)
```

## class as a Namespace

```python
from pprint import pprint as print

# some global variable
a = 10  #  __main__.a


def foo():  # __main__.foo
    a = 30  # __main__.foo.a
    print(id(a))

    def foo():  # __main__.foo.foo
        pass


class Namespace:  #  __main__.Namespace
    """Some documentation."""

    foo = "baz"  #  __main__.Namespace.foo

    def __init__(self):  # __main__.Namespace.__init__
        self.__dict__["foo"] = "bar"
        # self.foo = "bar"


breakpoint()  # TODO: remove
instance = Namespace()

print(Namespace.foo)
print(instance.foo)
```

## Enclosing

```python
from functools import partial

# can not change this function....
def runner(function):
    result = function()
    return result


def foo(message: str):
    print(f"Message from foo: {message}")


def main():
    tasks = []
    # runner(function=lambda: foo("some message 2"))
    # runner(function=partial(foo, "some message 3"))

    def _callback():
        nonlocal tasks
        task = create_task()
        tasks.append(task)
        return foo("some message 4")

    runner(function=_callback)


main()
```

## dependency injection

```python
def injector(func):
    def inner():
        user_input = input("Please enter the command: ")
        return func(user_input)

    return inner


@injector
def foo(user_input):
    print(f"result: {user_input}")


foo()
```

## error handler

```python
from functools import wraps


def error_handler(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Error: {error}")

    return inner


@error_handler
def panic():
    raise Exception("some message")


panic()
```

## logger

```python
"""
def foo(): ...

log(foo) => callable()

"""

from datetime import datetime
from functools import wraps


def log(save_to_file: bool = True):
    def wrapper(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            log_message = f"function {func.__name__} executed at {datetime.now()}"

            if save_to_file:
                print("saving to the JSON file")
            else:
                print(log_message)

        return inner

    return wrapper


@log(save_to_file=False)
def panic():
    print("I am panic")


def context1():
    pass

def context2():
    pass

@context1
func1()

@context2
func2()

@context2
func3()


def main():
    func1()
    func2()
    func3()

panic()
```
