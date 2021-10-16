# import abc
# from abc import ABC


# class Shape(ABC):
#     @abc.abstractmethod
#     def area(self):
#         # print("hello from A")
#         pass
#
#     def present(self):
#         print("hello")
#
#     @abc.abstractmethod
#     def perimeter(self):
#         pass
#
#
# class Triangle(Shape):
#
#     def __init__(self, *args):
#         self.a, self.b, self.c = args
#
#     def area(self):
#         # print("hello from A")
#         pass
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#
# class Square(Shape):
#
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         # print("hello from A")
#         pass
#
#     def perimeter(self):
#         return self.side * 4
#
#
# triangle_1 = Triangle(1, 2, 3)
# print(triangle_1.perimeter())

# class Person(object):
#     instance_ = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.instance_:
#             raise ValueError("This class is singleton")
#         cls.instance_ = super().__new__(cls)
#         return cls.instance_

# class Person(object):
#     instance_ = 0

#     def __new__(cls, *args, **kwargs):
#         cls.instance_ += 1
#         return super().__new__(cls)

#     def __init__(self, age, name):
#         self.name = name
#         self.age = age
#     #
#     # def __int__(self):
#     #     return 1
#     #

#     def __str__(self):
#         return f'{self.name} - {self.age}'

#     def __repr__(self):
#         return f'Person class object with name {self.name} - {self.age}'

#     def foo(self):
#         pass
#     def __eq__(self, other):
#         if not isinstance(other, Person):
#             raise ValueError("not comparable")
        
    

#         # return self.name == other.name and self.age == other.age
#         return self.foo() == other.foo()

#     def __ne__(self, other):
#         return not self.__eq__(other)

#     def __del__(self):
#         # print("object is deleted")
#         Person.instance_ -= 1


# person_1 = Person(25, 'John')
# # del person_1

# person_2 = Person(22, "John")
# person_3 = Person(22, "John")
# #
# # print(Person.instance_)
# #
# # text = 5
# # num = str(text)
# #
# # print([person_2, str(person_2)])

# print(person_2 == person_3)
# print(person_2 != person_3)


