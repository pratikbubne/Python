#
#
# # program 1
#
# class Student:
#     # this is a special method called constructor
#     def __init__(self):
#         self.name = "ravi"
#         self.age = "30"
#         self.marks = 900
#
#     # this is an instance method
#
#     def talk(self):
#         print(f'Hello , I am {self.name}')
#         print(f'Hello , My age is  {self.age}')
#         print(f'And , My marks are  {self.marks}')
#
# ravi = Student()
# print(ravi)
# ravi.talk()
#
# # A python program to create student objects with more than one
# # parameter
#
#
# class Student:
#     # this is a special method called constructor
#     def __init__(self, n ='',m=0): # Setting default parameters
#         self.name = n
#         self.marks = m
#
#     # this is an instance method
#
#     def display(self):
#         print(f'Hello , I am {self.name}')
#         print(f'And , My marks are  {self.marks}')
#
#
#  # calling the constructor with any arguments
#
# chinmay = Student()
# chinmay.display()
#
# # constructor with 2 arguments
# amol = Student("amol",900)
# amol.display()
#
#
# # Types of variables
#
# # Instance variables
# # class variables or Static variables
#
# # program 3
#
# # A program to understand the instance variable
#
# class Sample:
#
#     # this is a construtor
#
#     def __init__(self):
#         self.x = 10
#
#     def update(self):
#         self.x  = self.x + 1
#
# s1 =  Sample()
# s2 =  Sample()
# print(s1.x)
# print(s2.x)
#
# s1.update()
# print(s1.x)
# print(s2.x)
#
#
#
# class Sample:
#
#    # this is class variable
#     y = 10
#     # this is a construtor
#
#     def __init__(self):
#         self.x = 10
#
#     def update(self):
#         self.x  = self.x + 1
#
#     @classmethod
#     def modify(cls):
#         cls.y = cls.y + 1
#
# s1 =  Sample()
# s2 =  Sample()
# print(s1.x)
# print(s2.x)
# print(s1.y)
# print(s2.y)
# Sample.modify()
#
# print(s1.y)
# print(s2.y)
#
# s3 =  Sample()
#
# print(s3.y)
# # 11
#
# s3.y = 40
# print()


# types of methods

# class methods
# static methods

# instance -

#Accessor methods
#mutatoe methods

#program 5

# class Student:
#     def __init__(self, n = '',m = 0):
#         self.name = n
#         self.marks = m
#
#     # instance method
#
#     def display(self):
#         print(f'My name is  {self.name}')
#         print(f'My marks are {self.marks}')
#
#     # to calculate the grades based on marks
#
#     def calculateGrade(self):
#         if self.marks >= 600:
#             print('Grade A')
#         elif self.marks >= 500 and  self.marks < 600:
#             print('Grade B')
#         elif self.marks >= 300 and  self.marks < 500:
#             print('Grade C')
#         else:
#             print('Please try again')
#
# i = 1
#
# while(i <= 2):
#     name = input('Enter the name')
#     marks = int(input('Enter the marks'))
#     obj = Student(name,marks)
#
#     obj.display()
#     obj.calculateGrade()
#     i = i+1
#     print('*************************************')
#
#


class Bird:
    wing = 2
    # this is the class method
    @classmethod
    def fly(cls,name):
        print('{} flies with {} wings'.format(name,cls.wing))

Bird.fly('parrot')
Bird.fly('sparrow')


# number of objects for class

# static methods class varibales , instance information

# number of objects


class a():

    n= 0

    def __init__(self):
        a.n += 1 # short hand

    @staticmethod
    def count():
        print(a.n)

A =a()
B =a()
C =a()
D =a()

a.count()


# banking example

# name of person

# account

# depoist

# withdrawn

class Bank(object):

    def __init__(self,name,bal = 100):
        self.name = name
        self.bal = bal

    def depoist(self,amount):
        self.bal += amount
        return  self.bal

    def withdraw(self,amout):
        if self.bal  <= 100:
            print('Bal is less or equal to 100 , you can not withdraw'
                  '')
        else:
            self.bal = self.bal - amout
        return self.bal

name = input('Please enter your name')
abc = Bank(name)

while(True):
    print('d-depoist , w-withdrawl , e-exist ')
    a = input('Enter your choice')
    if a == 'd':
        amount=  int(input('Please the amount to depoist'))
        print(abc.depoist(amount))

    elif a == 'w':
        amount = int(input('Please the amount to depoist'))
        print(abc.withdraw(amount))

    elif a == 'e':
        break

    else:
        print('please enter the valid option')


# passing the class members  from one class to another

class Emp:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
    def display(self):
        print(self.id)
        print(self.name)
        print(self.salary)

class myClassB(object):

    @staticmethod
    def displayMethod(e):
        e.display()

    @staticmethod
    def calulateSalary(e):
        print(e.salary * 12)


emp = Emp(2,"chinmay",4000000)
myClassB.displayMethod(emp)
myClassB.calulateSalary(emp)


class Myclass:

    @staticmethod
    def sqa(x):
        print(x*x)

Myclass.sqa(5)
Myclass.sqa(10)

# Inner class

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.dob = self.Dob()

    def display(self):
        print('Name =',self.name)

    # user defined db
    class Dob:
        def __init__(self):
            self.dd = 10
            self.mm = 5
            self.yy = 1989
        def display(self):
            print(f'{self.dd}/{self.mm}/{self.yy}')
a = Person("chinmay",28)
a.dob.display()






















































# x = input('Please enter the expresson')
# print(x)
#
# x = eval(input('Please enter the expresson'))
# print(x)
#
# print(6+7)
#

