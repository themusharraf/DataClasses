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
# from dataclasses import dataclass, field
#
#
# def get_emp_id():
#     id = 2345
#     return id
#
#
# # A class for holding an employees content
# @dataclass
# class employee:
#     # Attributes Declaration
#     # using Type Hints
#     name: str
#     age: int
#
#     # default factory field
#     emp_id: str = field(default_factory=get_emp_id)
#     city: str = field(default="Tashkent")
#
#
# # object of dataclass
# emp = employee("Akbar", 21)
# print(emp)
# output
# employee(name='Akbar', age=21, emp_id=2345, city='Tashkent')


# init field example
from dataclasses import dataclass, field

# A class for holding an employees content
# @dataclass
# class Xodim:
#     # Attributes Declaration
#     # using Type Hints
#     name: str
#     age: int
#
#     # init field
#     emp_id: str
#     city: str = field(init=False, default="patna")
#
#
# # object of dataclass
# emp = Xodim("Hasan", "hasan858", 21)
# print(emp)


# repr field
# from dataclasses import dataclass, field
#
#
# # A class for holding an employees content
# @dataclass
# class Xodim:
#     # Attributes Declaration
#     # using Type Hints
#     name: str
#     age: int
#     emp_id: str
#     city: str = field(init=False, default="patna", repr=True)
#
#
# emp = Xodim("Jamshid", 21, "jama45"),
# print(emp)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __hash__(self):
#         return hash((self.name, self.age))
#
#     def __eq__(self, other):
#         return isinstance(other, Person) and self.name == other.name and self.age == other.age
#
#
# # Create instances of the Person class
# person1 = Person("Alice", 30)
# person2 = Person("Alice", 30)
#
# # Print custom hash codes
# print(hash(person1))
# print(hash(person2))

# from dataclasses import dataclass
#
#
# @dataclass
# class Person:
#     name: str
#     age: int
#
#     def __hash__(self):
#         return hash((self.name, self.age))
#
#
# person1 = Person("Alisa", 30)
# person2 = Person("Javohir", 30)
#
# print(hash(person1))
# print(hash(person2))


# hash
# from dataclasses import dataclass, field
#
#
# # A class for holding an employees content
# @dataclass(unsafe_hash=True)
# class Xodim:
#     # Attributes Declaration
#     # using Type Hints
#     name: str
#     age: int
#     emp_id: str
#     city: str = field(init=False, default="patna",
#                       repr=True, hash=False, compare=True)
#
#
# emp1 = Xodim("Ali", "ali8", 24)
# emp2 = Xodim("Husan", "husan14", 22)
# print(emp1 == emp2)
# output
# false

# A basic Data Class
# importing dataclass module
# from dataclasses import dataclass, field
#
#
# # parent class
# @dataclass
# class Staff:
#     name: str
#     emp_id: str
#     age: int
#
#
# # child class
# @dataclass
# class employee(Staff):
#     salary: int
#
#
# emp = employee("Ulug'bek", "useryou44", 21, 60000)
# print(emp)


















