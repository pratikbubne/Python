


# Abstract class has no objects
from abc import ABC, abstractmethod

class classA(ABC):
    @abstractmethod
    def calculate(self,x):
        pass


class Square(classA):
    def calculate (self, x):
        print(x * x)

class Cube(classA):
    def calculate(self, x):
        print(x * x * x)

#a = classA()

s = Square()
s.calculate(3)



#  loan()   save()




from abc import ABC, abstractmethod

class WB(ABC):
    @abstractmethod
    def loan(self):
        pass

    @abstractmethod
    def save(self):
        pass

class SBI(WB):

    def loan(self):
        print('loan method called ')

    def save(self):
        print('save method called')


class BOM(WB):

    def loan(self):
        print('loan method called BOM')

    def save(self):
        print('save method called BOM')



w = BOM()
w.loan()
w.save()

# ----- program One


from abc import ABC , abstractmethod
class WorldBank(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def loan(self):
        pass

class SBI(WorldBank):
    def save(self):
        print('saving method from the SBI')
    def loan(self):
        print('loan method from the SBI')

class BOM(WorldBank):
    def save(self):
        print('saving method from the SBI')
    def loan(self):
        print('loan method from the SBI')


w = BOM()

w.loan()
w.save()


class Car(ABC):
    # function
    # Function constructor
    # instance variables

    def __init__(self,regno):
        self.regno = regno

    def openTank(self):
        print(f'The tank is for the petrol  and car is {self.regno}')

    @abstractmethod
    def steering(self):
        pass

    @abstractmethod
    def start(self):
        pass

class Maruti(Car):

    # def __init__(self, a,regno):
    #     super().__init__(regno)
    #     self.a = a
    #

    def steering(self):
        print("power")

    def start(self):
        print('automatic')


class Audi(Car):

    # def __init__(self, a,regno):
    #     super().__init__(regno)
    #     self.a = a
    #

    def steering(self):
        print("power full auotmatic")

    def start(self):
        print('full automaic start')

w = Maruti(123)
w.openTank()

a = Audi(123)
w.openTank()
w.steering()

class DBconnect(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class Oracle(DBconnect):

    def connect(self):
        print('oracle db connected')

    def disconnect(self):
        print('oracle db disconnected')


class Postgres(DBconnect):
    def connect(self):
        print('Postgres db connected')

    def disconnect(self):
        print('Postgres db disconnected')

class Mysql(DBconnect):
    def connect(self):
        print('Mysql db connected')

    def disconnect(self):
        print('Mysql db disconnected')

class DataBase:

    str = input('Which db you want to connected') # Oracle
    className = globals()[str] # Oracle
    s = className()  #    s = Oracle()
    s.connect()  # s.connect()
    s.disconnect() # s.disconnect()

# ----
# Django

# 7 -- logical
# Files
#
# Regular  expression
#
# Exception  handling
#
# Multi threading
#
# List comprehence
#
# Functions
#
# Arrays

# Django ... Rest api











































