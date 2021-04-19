# class Person():
#     age = 10
#     color ="fair"
#
#     def printAge(self):
#         print(self.age , self.color)
#
#
#
# raju = Person()
# ram = Person()
#
# print(raju.age)
# raju.age = 50
#
# print(ram.age) # 10
# print(raju.age) # 50
#
# # attributes methods
#
#
# name = "chinmay"
# print(type(name))
#
# class person():
#
#     # attributes or properties
#     name = "chinmay"
#     age = 30
#
#     def displayName(self):
#         print(self.name , self.age)
#
#
# chinmay = person()
# jinendra = person()
#
# chinmay.age = 45
# print(chinmay.age) # 45
# print(jinendra.age) # 30
#
#
# chinmay.displayName() # self ----chinmay
# jinendra.displayName() # self ---- jinendra
#

# 3 ways to  handle class variables

#1) outside the class

#2)  Using getter and setter function

#3) Using contructor



# class person():
#
#     age = 10
#
#
#     def display(self):
#         print(self.age)
#
#
# # Getting the for instance variable outside the class
#
# amit = person()
# amit.age = 45
# print(amit.age)

# Getter and setter method


class Person():

    age = 10

    def setAge(self,x): # parameter
        self.age = x  # 100

    def getAge(self):
        print(self.age)

sweta =Person()

sweta.setAge(20)
print(sweta.age)
#Getter and setter method

chinmay = Person()
chinmay.getAge()
chinmay.setAge(100)
chinmay.getAge()

# setting the instance variable using contructor ,

# As soon as the object is created , constructor is called



class Person():

    # Fuction constructor

    def __init__(self,x):
        self.age = x

    def display(self):
        print(self.age)

    def updateAge(self,x):
        self.age = x
        print(f'Update value {self.age}')

chinmay = Person(10)
sweta = Person(20)
sweta.updateAge(200)
sweta.age = 300



class person():

    def __init__(self,name,age):
        self.age = age
        self.name = name

    def display(self):
        print(self.name , self.age)

liobj = []

for item in range(2):

    name = input('Enter name')
    age = input ('Enter age')
    liobj.append(person(name,age))


print(liobj)
# class Person():
#     age = 10
#     color ="fair"
#
#     def printAge(self):
#         print(self.age , self.color)
#
#
#
# raju = Person()
# ram = Person()
#
# print(raju.age)
# raju.age = 50
#
# print(ram.age) # 10
# print(raju.age) # 50
#
# # attributes methods
#
#
# name = "chinmay"
# print(type(name))
#
# class person():
#
#     # attributes or properties
#     name = "chinmay"
#     age = 30
#
#     def displayName(self):
#         print(self.name , self.age)
#
#
# chinmay = person()
# jinendra = person()
#
# chinmay.age = 45
# print(chinmay.age) # 45
# print(jinendra.age) # 30
#
#
# chinmay.displayName() # self ----chinmay
# jinendra.displayName() # self ---- jinendra
#

# 3 ways to  handle class variables

#1) outside the class

#2)  Using getter and setter function

#3) Using contructor



# class person():
#
#     age = 10
#
#
#     def display(self):
#         print(self.age)
#
#
# # Getting the for instance variable outside the class
#
# amit = person()
# amit.age = 45
# print(amit.age)

# Getter and setter method


class Person():

    age = 10

    def setAge(self,x): # parameter
        self.age = x  # 100

    def getAge(self):
        print(self.age)

sweta =Person()

sweta.setAge(20)
print(sweta.age)
#Getter and setter method

chinmay = Person()
chinmay.getAge()
chinmay.setAge(100)
chinmay.getAge()

# setting the instance variable using contructor ,

# As soon as the object is created , constructor is called



class Person():

    # Fuction constructor

    def __init__(self,x):
        self.age = x

    def display(self):
        print(self.age)

    def updateAge(self,x):
        self.age = x
        print(f'Update value {self.age}')

chinmay = Person(10)
sweta = Person(20)
sweta.updateAge(200)
sweta.age = 300



class person():

    def __init__(self,name,age):
        self.age = age
        self.name = name

    def display(self):
        print(self.name , self.age)

liobj = []

for item in range(2):

    name = input('Enter name')
    age = input ('Enter age')
    liobj.append(person(name,age))


print(liobj)


for item in liobj:
    item.display()













for item in liobj:
    item.display()











