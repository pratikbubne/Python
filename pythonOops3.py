#
#
# # class Father(object):
# #
# #     # instance variable
# #     def __init__(self):
# #         self.property = 800
# #
# #     # instance method
# #     def display(self):
# #         print(self.property)
# #
# # class Son(Father):
# #     pass
# #
# # s = Son()
# # s.display()
#
#
# # ---------------------------
#
# # # parent properties and method override
# # class Father(object):
# #
# #     # instance variable
# #     def __init__(self):
# #         self.property = 800
# #
# #     # instance method
# #     def display(self):
# #         print(self.property)
# #
# # class Son(Father):
# #     def __init__(self):
# #         self.property = 900
# #
# #     # instance method
# #     def display(self):
# #         print(self.property)
# #
# #
# # s = Son()
# # s.display()
#
# # using  parameterized construtor
#
# class Father(object):
#
#     def __init__(self,property):
#         self.property = property
#
#     def display(self):
#         print(self.property)
#
# class Son(Father):
#
#     def __init__(self,property,sproperty):
#         super().__init__(property)
#         self.sproperty = sproperty
#
#     def display(self):
#         print(self.sproperty)
#         super().display()
#
# s = Son(100,200)
# s.display()
#
# # --------------------------
# #accssor and modifier
#
#
# class Student():
#
#     # 3 instance variable
#
#     def setId(self,id):
#         self.id = id
#
#     def getId(self):
#         return self.id
#
#     def setName(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
#     def setAddress(self, address):
#         self.address = address
#
#     def getAddress(self):
#         return self.address
#
#     def setmarks(self, marks):
#         self.marks = marks
#
#     def getMarks(self):
#         return self.marks
#
# class Teacher(Student):
#
#     def setSalary(self,salary):
#         self.salary = salary
#
#     def getSalry(self):
#         return self.salary
#
# t = Teacher()
#
# t.setId(20)
# t.setName("ram")
# t.setAddress("Pune")
# t.setSalary(100000)
#
# y = t.getId()
# print(y)
#
# print(t.getName())
# print(t.getAddress())
# print(t.getSalry())
#
# #----------------------------------------------
#
# # class method
# class Bank():
#     cash = 20000000
#     @classmethod
#     def display(cls):
#         print(cls.cash)
#
# class Pbank(Bank):
#     cash = 30000000
#     @classmethod
#     def display(cls):
#         print(cls.cash + Bank.cash)
#
# g = Pbank()
# g.display()
#
# Bank().display()
#
# # ---------------------
#
# # Method order resolution
#
# class A(object):
#     def method(self):
#         print('A class method called')  #3
#         super().method()
#
# class B(object):
#     def method(self):
#         print('B class method called')  # 5
#         super().method()
#
# class C(object):
#     def method(self):
#         print('C class method called')  # 6
#
# class X(A,B):
#     def method(self):
#         print('X class method called')   # 2
#         super().method()
#
# class Y(B,C):
#     def method(self):
#         print('Y class method called')  # 4
#         super().method()
#
# class P(X,Y,C):
#     def method(self):
#         print('P class method called')   # 1
#         super().method()
#
# p = P()
# p.method()
#
# # class Father(object):
# #
# #     # instance variable
# #     def __init__(self):
# #         self.property = 800
# #
# #     # instance method
# #     def display(self):
# #         print(self.property)
# #
# # class Son(Father):
# #     pass
# #
# # s = Son()
# # s.display()
#
#
# # ---------------------------
#
# # # parent properties and method override
# # class Father(object):
# #
# #     # instance variable
# #     def __init__(self):
# #         self.property = 800
# #
# #     # instance method
# #     def display(self):
# #         print(self.property)
# #
# # class Son(Father):
# #     def __init__(self):
# #         self.property = 900
# #
# #     # instance method
# #     def display(self):
# #         print(self.property)
# #
# #
# # s = Son()
# # s.display()
#
# # using  parameterized construtor
#
# class Father(object):
#
#     def __init__(self,property):
#         self.property = property
#
#     def display(self):
#         print(self.property)
#
# class Son(Father):
#
#     def __init__(self,property,sproperty):
#         super().__init__(property)
#         self.sproperty = sproperty
#
#     def display(self):
#         print(self.sproperty)
#         super().display()
#
# s = Son(100,200)
# s.display()
#
# # --------------------------
# #accssor and modifier
#
#
# class Student():
#
#     # 3 instance variable
#
#     def setId(self,id):
#         self.id = id
#
#     def getId(self):
#         return self.id
#
#     def setName(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
#     def setAddress(self, address):
#         self.address = address
#
#     def getAddress(self):
#         return self.address
#
#     def setmarks(self, marks):
#         self.marks = marks
#
#     def getMarks(self):
#         return self.marks
#
# class Teacher(Student):
#
#     def setSalary(self,salary):
#         self.salary = salary
#
#     def getSalry(self):
#         return self.salary
#
# t = Teacher()
#
# t.setId(20)
# t.setName("ram")
# t.setAddress("Pune")
# t.setSalary(100000)
#
# y = t.getId()
# print(y)
#
# print(t.getName())
# print(t.getAddress())
# print(t.getSalry())
#
# #----------------------------------------------
#
# # class method
# class Bank():
#     cash = 20000000
#     @classmethod
#     def display(cls):
#         print(cls.cash)
#
# class Pbank(Bank):
#     cash = 30000000
#     @classmethod
#     def display(cls):
#         print(cls.cash + Bank.cash)
#
# g = Pbank()
# g.display()
#
# Bank().display()
#
# # ---------------------
#
# # Method order resolution
#
# class A(object):
#     def method(self):
#         print('A class method called')  #3
#         super().method()
#
# class B(object):
#     def method(self):
#         print('B class method called')  # 5
#         super().method()
#
# class C(object):
#     def method(self):
#         print('C class method called')  # 6
#
# class X(A,B):
#     def method(self):
#         print('X class method called')   # 2
#         super().method()
#
# class Y(B,C):
#     def method(self):
#         print('Y class method called')  # 4
#         super().method()
#
# class P(X,Y,C):
#     def method(self):
#         print('P class method called')   # 1
#         super().method()
#
# p = P()
# p.method()
#
#
# # Encapsulatio  --- class
#
# # Inheritance
#
# # polymorphism
#
#
# # Duck typing philosophy of python
# # Method over-rinding
# # Method over-overloading
# # Operation overloading
#
# class Duck:
#     def talk(self):
#         print('quack quack')
#
# class Human:
#     def talk(self):
#         print('Hello hi')
#
# def cal_talk(obj):
#     obj.talk()
#
#
# ram = Human()
# rat = Duck()
#
# cal_talk(ram)
#
#
# # Overriding
#
# # different class , same method name , same signature
#
# class WorldBank(object):
#
#     def saving(self):
#         print('saving 2 percent')
#
# class SBI(WorldBank):
#
#     def saving(self):
#         print('saving 4 percent')
#
# f = SBI()
# f.saving()
#
# # same class same method name , different signature
#
# # overloading in python
#
# class Add(object):
#     def add(a = None , b = None ,c = None):
#         if a != None and b != None and c != None:
#             print(a + b + c)
#
#         elif a != None and b != None:
#             print(a + b)
#
#         else :
#             print('Enter the correct input ')
#
# a = Add()
#
# a.add(1,3,4)
# a.add(3,3)
# a.add()
#
#
# class Dog:
#
#     def bark(self):
#         print('Bow , wow !')
#
# class Duck:
#     def talk(self):
#         print('quack quack')
#
# class Human:
#     def talk(self):
#         print('Hello hi')
#
# def cal_talk(obj):
#
#     if hasattr(obj, 'talk'):
#         obj.talk()
#     elif hasattr(obj, 'bark'):
#         obj.bark()
#     else:
#         print('Wrong obj passed ')
#
#
# d = Dog()
# cal_talk(d)
#
# # duck typing
# # overloading
# # overriding
# # operator
#
print(2+3)  # 5
print('chinmay'+'deshpande') # string
print([1,2,3]+[3,4,5])
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # v = 10
# # t = 20
# #
# #
# # def add(x,y):
# #     print(x+y)
# #
# # add(v,t)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # Encapsulatio  --- class
#
# # Inheritance
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # v = 10
# # t = 20
# #
# #
# # def add(x,y):
# #     print(x+y)
# #
# # add(v,t)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


# search(1,3,4)
# search(1,3)
# search('iphone')

# print(2+3)  # 5
# print('chinmay'+'deshpande') # string
# print([1,2,3]+[3,4,5])


# class Bookx(object):
#     def __init__(self,pages):
#         self.pages = pages
#
# class Booky(object):
#     def __init__(self, pages):
#         self.pages = pages
#     def __add__(self, other):
#         print(self.pages  + other.pages)
#
# s = Bookx(100)
# s1 = Booky(200)
# s + s1  # adding two objects by operator overloading


# class Bookx(object):
#     def __init__(self,pages):
#         self.pages = pages
#
# class Booky(object):
#     def __init__(self, pages):
#         self.pages = pages
#
#     def __sub__(self, other):
#         print(self.pages - other.pages)
#
# s = Bookx(100)
# s1 = Booky(200)

#s1-s # subtraction between two objects using operator overloading '-'
#
# class Bookx(object):
#     def __init__(self,pages):
#         self.pages = pages
#
# class Booky(object):
#     def __init__(self, pages):
#         self.pages = pages
#
#     def __gt__(self, other):
#        print(self.pages > other.pages)
#
# s = Bookx(500)
# s1 = Booky(200)
#
# s1 > s

# -------------

# overloading

import math
class Square:
    def area(self,x):
        print(x * x)
        return x*x

class Circle(Square):
    def area(self,x):
        print(math.pi * x * x)

s = Square(23)
s.area()

d = Circle(3)
d.area()






