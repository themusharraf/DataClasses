# A basic Data Class
# importing dataclass module
# from dataclasses import dataclass
#
# @dataclass
# class employee:
#     # Attributes  using Type Hints
#     name: str
#     emp_id: str
#     age: int
#     city: str
#
#
# emp1 = employee("Omina", "ans24", 21, 'samarkand')
# emp2 = employee("Akbar", "auth23", 28, 'bukhara')
# emp3 = employee("Zilola", "zilol18", 21, 'Tashkent')
#
# print("xodimlar ob'ekti :")
# print(emp1)
# print(emp2)
# print(emp3)
#
# # referring two object to check equality
# print("emp1 va emp2 ma'lumotlari bir xilmi? ", emp1 == emp2)
# print("emp1 va emp3 ma'lumotlari bir xilmi?", emp1 == emp3)
#
# from dataclasses import dataclass
#
#
# #
# #
# # A class for holding an employees content
# @dataclass
# class employee:
#     # Attributes Declaration
#     # using Type Hints
#     name: str
#     emp_id: str
#     age: int
#     city: str
#
#
# # object of the class
# emp = employee("Musharraf", "allnc9", 23, 'Tashkent')
#
# print(emp.__dataclass_fields__)

# default field example
# from dataclasses import dataclass, field
# @dataclass
# class employee:
#     # Attributes Declaration
#     # using Type Hints
#     name: str
#     emp_id: str
#     age: int
#
#     # default field set
#     # city : str = "patna"
#     city: str = field(default="Tashkent")
#
# emp = employee("Dilshod", "dilshod001", 21)
# print(emp)
# # output
# # employee(name='Dilshod', emp_id='dilshod001', age=21, city='Tashkent')


# default factory example
from dataclasses import dataclass, field


def get_emp_id():
    id = 2345
    return id


# A class for holding an employees content
@dataclass
class employee:
    # Attributes Declaration
    # using Type Hints
    name: str
    age: int

    # default factory field
    emp_id: str = field(default_factory=get_emp_id)
    city: str = field(default="Tashkent")


# object of dataclass
emp = employee("Akbar", 21)
print(emp)
# output
# employee(name='Akbar', age=21, emp_id=2345, city='Tashkent')
