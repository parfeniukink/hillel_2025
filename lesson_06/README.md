# Meeting summary


Meeting summary for Заняття 6 | Python Pro (21.11.2024) Дмитро Парфенюк (12/12/2024)

Quick recap

Зустріч була присвячена об’єктно-орієнтованим концепціям програмування на Python, що охоплюють класи, методи, поліморфізм та їх практичне застосування. Дмитро вів дискусії про структурування коду за допомогою класів, підкресливши важливість поділу логічних блоків і уникнення зайвої складності. Команда досліджувала різні приклади та реалізації, включаючи систему управління даними студентів, обговорюючи переваги та проблеми використання класів у проектах програмування.

Next steps
• Студенти для перегляду відеозапису класу для кращого розуміння складних тем, що охоплюються.
• Студенти мають записати список незрозумілих тем та надіслати Дмитру для отримання потенційного додаткового пояснювального відео.
• Студенти практикують написання коду, щоб краще зрозуміти і засвоїти концепції, обговорювані.
• На наступному уроці Дмитру належить закінчити приклади уроку.
• Дмитру після завершення основного базового матеріалу прикриють вирази крипти.
• Дмитру призначать домашнє завдання після покриття виразів крипти.
• Студенти для завершення рефакторингу студентського проекту, використовуючи класний підхід, обговорюваний.
• Студенти для реалізації класу IO Manager для обробки користувальницьких вхідних і файлових операцій.
• Студенти для реалізації класу університету для управління студентськими даними та операціями.
• Студенти реалізують Студентський клас з відповідними атрибутами і методами.
• Студенти рефакторингу існуючих функцій у відповідні методи класу.
• Студенти для тестування рефакторированной програми для забезпечення належної функціональності.

Summary

Класи Python, простори імен і методи
Дмитро провів дискусію щодо концепцій класів, просторів імен та методів програмування Python. Він пояснив різницю між функціями і методами, підкресливши, що методи є частиною класу і можуть бути статичними або прив'язаними до конкретних даних. Дмитро також обговорив вбудовану бібліотеку та її методи, такі як «title», «join», «strip» та «sort». Він підкреслив важливість розуміння цих концепцій для ефективного кодування і закликав команду експериментувати з методами. Розмова завершилася тим, що Дмитро запропонував представити документ, узагальнюючи практичні методи, які потрібно запам’ятати.

Реалізація поліморфізму в ООП
На зустрічі Дмитро пояснює концепцію поліморфізму в об’єктно-орієнтованому програмуванні (ООП) та демонструє, як реалізувати просту систему виробництва продуктів з використанням принципів ООП на Python. Він створює базовий клас продукту з назвою і ціновими атрибутами, і пропонує створити окремі класи для різних компаній, таких як Tesla і Intel, щоб інкапсулювати їх специфічну логіку. Дискусія фокусується на використанні ООП для моделювання реальних сценаріїв і використання таких концепцій, як успадкування, абстракція і поліморфізм для повторного використання коду і ремонтопридатності.
Розуміння структури класів у програмуванні
Дмитро обговорив важливість розуміння логічної структури класів у програмуванні. Він підкреслив, що класи часто виконують дві основні функції: проведення поведінкової структури або дії та управління даними. Він також підкреслив важливість розділення логічних блоків у програмі, щоб уникнути неефективності та непотрібного використання даних. Дмитро використовував приклади, щоб проілюструвати свої точки зору, такі як потенціал класу бути одночасно і рішенням даних, і алгоритмом. Він також закликав команду розглядати парадигму класів як шаблони, а не просто контейнери даних. Розмова закінчилася тим, що Дмитро запропонував команді добре структурувати свій код і поєднувати функції лише тоді, коли логіка стане зрозумілою.

Структура та функціональність проекту
Дмитро обговорив структуру та функціонал проекту, який передбачає введення користувачем, обробку даних та умовну інформацію. Він пояснив, як проект розділений на логічні блоки, з головним контролером обробки вхідних даних і кодовим помічником, який надає відповіді. Дмитро також обговорив використання класів та послуг у проекті, підкресливши переваги абстракції та поділу концернів. Він наголосив на важливості врахування складності проекту та необхідності ефективного розвитку. Дмитро також торкнувся концепції запасного сервісу, який надає тестові дані в режимі налагодження та реальні дані у виробничому режимі. На завершення він продемонстрував, як реалізувати єдиний інтерфейс для різних класів, на прикладі базового продукту з білл-функцією.
Нова функціональність та класова ієрархія
Дмитро розповів про впровадження нового функціоналу в їх системі, який дозволяє легко отримати доступ до будь-якого з двох класів. Він продемонстрував, як додати конкретну інформацію про те, хто виконував продукт, і пояснив концепцію ієрархії класів. Дмитро також обговорив використання відладчика, пояснивши, як його можна використовувати для відображення даних та налагоджувального коду. Він наголосив на важливості розуміння різниці між внутрішнім і зовнішнім відображенням об’єктів у системі. Дмитро також обговорив потенціал розширення класів з додатковим функціоналом і важливість чіткої ієрархії залежностей. Він попередив про потенційну плутанину, якщо класи імітуються один в одного, що призводить до непередбачених наслідків.

Уникнення імітації класу в програмуванні
Дмитро обговорив важливість уникнення імітації класів у програмуванні, оскільки це може призвести до плутанини та потенційних проблем. Замість цього він рекомендував використовувати композицію, яка включає в себе інкапсулювання об'єктів всередині класу. Дмитро також пояснив поняття композиції щодо класової взаємодії та використання асоціацій, агрегації та композиції. Він також проілюстрував переваги композиції, такі як уникнення необхідності пошуку методів в декількох класах і можливість створення окремих класів для конкретних сервісів. Ганна брала участь в обговоренні, задаючи питання і уточнюючи концепції, що обговорювалися.
Заняття з програмування: переваги та недоліки
Дмитро провів дискусію щодо використання класів у програмуванні, акцентуючи увагу на їх перевагах та недоліках. Він пояснив, що класи зручні для модульної композиції, особливо при роботі з великою кількістю об'єктів. Однак він також зазначив, що класи можуть стати надлишковими і складними, коли в них багато методів. Дмитро запропонував використовувати класи для опису єдиної логіки, і він продемонстрував це рефакторингом проекту для використання класів для читання та запису файлів. Він також попросив відгук про те, чи було гарною ідеєю використовувати заняття для різних аспектів проекту, таких як історія студентів. Учасники в цілому погодилися, що заняття були корисними, але можуть бути складними в управлінні.

Заняття з програмування та абстракції
Дмитро та Дар’я обговорили концепцію класів у програмуванні, зосередивши увагу на їх ролі в інкапсуляції даних та методах роботи з цими даними. Вони досліджували ідею класів як способу організації та структурування даних, а Дмитро наводив приклади того, як класи можуть бути використані для представлення різних рівнів абстракції, таких як всесвіт, фізика та соціальні структури. Ганна долучилася до дискусії, поставивши під сумнів необхідність занять і запропонувавши альтернативні підходи, такі як зберігання даних в окремих файлах. Команда також обговорила потенціал вкладення класів і важливість вибору правильного рівня деталізації при створенні класів.
Об'єктно-орієнтоване програмування для даних студентів
На зустрічі Дмитро обговорює, як структурувати програму управління студентськими даними з використанням принципів об’єктно-орієнтованого програмування на Python. Він пропонує створити студентський клас для представлення окремих студентів, а також університетський клас для обробки таких операцій, як додавання, оновлення та отримання студентських даних. Він також пропонує мати клас InputOutputManager для обробки користувацьких операцій введення/виведення та файлів. Дискусія зосереджена на поділі проблем, дотримуючись хороших принципів проектування програмного забезпечення та проводячи паралелі з архітектурами реальних веб-додатків. Дмитро наголошує на важливості написання коду для розуміння понять, а не просто читання коду.


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

- `str.upper()`: Converts all characters to uppercase.
- `str.lower()`: Converts all characters to lowercase.
- `str.capitalize()`: Capitalizes the first character.
- `str.title()`: Converts the string to title case.
- `str.strip()`: Removes leading and trailing whitespace.
- `str.lstrip()`: Removes leading whitespace.
- `str.rstrip()`: Removes trailing whitespace.
- `str.replace(old, new)`: Replaces all occurrences of old with new.
- `str.split(separator)`: Splits the string into a list based on the separator.
- `str.join(iterable)`: Joins elements of an iterable with the string.
- `str.startswith(prefix)`: Returns True if the string starts with the given prefix.
- `str.endswith(suffix)`: Returns True if the string ends with the given suffix.
- `str.find(substring)`: Returns the lowest index of the substring, or -1 if not found.
- `str.index(substring)`: Like find() but raises a ValueError if not found.
- `str.isalpha()`: Returns True if all characters are alphabetic.
- `str.isdigit()`: Returns True if all characters are digits.
- `str.isalnum()`: Returns True if all characters are alphanumeric.
- `str.isspace()`: Returns True if all characters are whitespace.
- `str.count(substring)`: Returns the number of non-overlapping occurrences of the substring.

## 2. List (list) Methods:

- `list.append(item)`: Adds item to the end of the list.
- `list.insert(index, item)`: Inserts item at the specified index.
- `list.remove(item)`: Removes the first occurrence of item.
- `list.pop([index])`: Removes and returns the item at index, or the last item if index is not specified.
- `list.clear()`: Removes all items from the list.
- `list.index(item)`: Returns the index of the first occurrence of item.
- `list.count(item)`: Returns the number of occurrences of item.
- `list.sort()`: Sorts the list in ascending order.
- `list.reverse()`: Reverses the list in place.
- `list.extend(iterable)`: Extends the list by appending elements from an iterable.

## 3. Dictionary (dict) Methods:

- `dict.get(key, default=None)`: Returns the value for key if it exists, otherwise returns default.
- `dict.keys()`: Returns a view object with all the dictionary's keys.
- `dict.values()`: Returns a view object with all the dictionary's values.
- `dict.items()`: Returns a view object with the dictionary’s key-value pairs.
- `dict.update(other_dict)`: Updates the dictionary with another dictionary's key-value pairs.
- `dict.pop(key)`: Removes the key and returns its value, or raises a KeyError.
- `dict.popitem()`: Removes and returns the last inserted key-value pair.
- `dict.clear()`: Removes all items from the dictionary.
- `dict.setdefault(key, default=None)`: Returns the value if the key exists, otherwise inserts the key with the default value.

## 4. Tuple (tuple) Methods:

- `tuple.count(item)`: Returns the number of occurrences of item.
- `tuple.index(item)`: Returns the index of the first occurrence of item.

## 5. Set (set) Methods:

- `set.add(item)`: Adds item to the set.
- `set.remove(item)`: Removes item from the set, raises a KeyError if not found.
- `set.discard(item)`: Removes item from the set if it is present, does nothing if not found.
- `set.pop()`: Removes and returns an arbitrary element from the set.
- `set.clear()`: Removes all elements from the set.
- `set.union(other_set)`: Returns the union of sets.
- `set.intersection(other_set)`: Returns the intersection of sets.
- `set.difference(other_set)`: Returns the difference of sets.
- `set.symmetric_difference(other_set)`: Returns the symmetric difference of sets.
- `set.update(other_set)`: Updates the set with the union of sets.
- `set.intersection_update(other_set)`: Updates the set with the intersection.
- `set.difference_update(other_set)`: Updates the set with the difference.
- `set.symmetric_difference_update(other_set)`: Updates the set with the symmetric difference.

## 6. Integer (int) Methods:

- `int.bit_length()`: Returns the number of bits required to represent the integer in binary.
- `int.to_bytes(length, byteorder)`: Returns an array of bytes representing the integer.
- `int.from_bytes(bytes, byteorder)`: Converts a byte array back into an integer.
- `int.__add__()`, int.**sub**(), etc.: Magic methods for arithmetic operations like addition, subtraction, etc.

## 7. Float (float) Methods:

- `float.is_integer()`: Returns True if the float is an integer (e.g., 3.0).
- `float.as_integer_ratio()`: Returns a tuple of integers representing the float as a ratio.
- `float.hex()`: Returns a hexadecimal representation of the float.
- `float.fromhex(string)`: Converts a hexadecimal string to a float.

## 8. Boolean (bool) Methods:

- `bool.__and__(other)`: Logical AND operation.
- `bool.__or__(other)`: Logical OR operation.
- `bool.__xor__(other)`: Logical XOR operation.

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
