"""
Generators
"""


class Student:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def __str__(self) -> str:
        return f"Student {self.name}"


# 4000
group: list[Student] = [
    Student("John"),
    Student("John"),
    Student("Marry"),
    Student("John"),
    Student("Marry"),
    Student("Marry"),
    Student("John"),
    Student("Marry"),
    Student("John"),
    Student("Mark"),
    Student("Mark"),
    Student("Marry"),
    Student("Mark"),
]

# 1000.count("john")
# 1000.count("marry")
# 1000.count("john")
# 1000.count("marry")

# 1: 1 from data, 1..1000 in data for count
# 2: 2 from data, 1..1000 in data for count
# 1 000 000



# 1: 1 from data, 1 if/else...
# 2: 1 from data, 1 if/else...

# def deduplicate(data: list[Student]) -> list[Student]:
#     existing_names: set[str] = set()
#     results: list[Student] = []


#     for student in data:
#         if data.count(student.name) == 1:
#             results.append(student)

#         if student.name not in existing_names:
#             results.append(student)
#             existing_names.add(student.name)

#     return results


def deduplicate(data: list[Student]):
    existing_names: set[str] = set()

    for student in data:
        if student.name not in existing_names:
            yield student
            existing_names.add(student.name)


for student in deduplicate(group):
    print(student)
