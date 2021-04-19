

# prgram One - multi -level



class Person():

    age = 10  # class variable


    def __init__(self,age,name):  # instance varaible
        self.age = age
        self.name = name

    #@class annotations to update the method

    @classmethod
    def changeX(cls):
        cls.x = 20


    # Chaging the instance varaible // Getter Setter
    def changeAge(self):
        self.age = 40

    @staticmethod
    def printInformation():
       print('hello')




Person.changeX()
Person.printInformation()

v = Person(29,31)


# -----

#outside the class

# Getter and setter

# constructor

# Multi -level # multiple inheritance

class Grandfather(object):
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def Gname(self):
        print(self.firstName , self.lastName)

# Inheritance
class Father(Grandfather):

    def __init__(self, lastName,Ffathername, GfirstName):
        super().__init__(GfirstName,lastName)
        self.FfirstName = Ffathername

    def Fname(self):
        print(self.FfirstName, self.lastName)


class Son(Father):

    def __init__(self, lastName,firstname ,Ffathername, GfirstName):
        super().__init__(lastName,Ffathername,GfirstName)
        self.SfirstName = firstname

    def Sname(self):
        print(self.SfirstName, self.lastName)

son = Son("deshpande","chinmay","shirish","manohar") # function constructor

son.Gname()
son.Fname()
son.Sname()

# single inheritance

class Mother(object):

    def __init__(self,lastName,Mfirstname):
        self.Mfirstname = Mfirstname
        self.lastName = lastName

    def displayName(self):
        print(self.Mfirstname,self.lastName)


class Son(Mother):

    def __init__(self, lastName, Mfirstname,sfirstName):
        super().__init__(lastName,Mfirstname,)
        self.sfirstName = sfirstName


    def displayName(self):
        print(self.sfirstName, self.lastName)
        super().displayName()

class Daughter(Mother):

    def __init__(self, lastName, Mfirstname,dfirstName):
        super().__init__(lastName,Mfirstname,)
        self.dfirstName = dfirstName

    def displayName(self):
        print(self.dfirstName, self.lastName)
        super().displayName()
print('****************')
chinmay = Son('deshpande','kanchan','chinmay')
chinmay.displayName()
gauri = Daughter('deshpande','kanchan','gauri')
gauri.displayName()
kanchan = Mother('deshpande','Kanchan')
kanchan.displayName()

# Multiple inheritance

class Maternal(object):
    def __init__(self,lastname):

        self.lastname =lastname
        print(self.lastname,"maternal")


# prgram One - multi -level



class Person():

    age = 10  # class variable


    def __init__(self,age,name):  # instance varaible
        self.age = age
        self.name = name

    #@class annotations to update the method

    @classmethod
    def changeX(cls):
        cls.x = 20


    # Chaging the instance varaible // Getter Setter
    def changeAge(self):
        self.age = 40

    @staticmethod
    def printInformation():
       print('hello')




Person.changeX()
Person.printInformation()

v = Person(29,31)


# -----

#outside the class

# Getter and setter

# constructor

# Multi -level # multiple inheritance

class Grandfather(object):
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def Gname(self):
        print(self.firstName , self.lastName)

# Inheritance
class Father(Grandfather):

    def __init__(self, lastName,Ffathername, GfirstName):
        super().__init__(GfirstName,lastName)
        self.FfirstName = Ffathername

    def Fname(self):
        print(self.FfirstName, self.lastName)


class Son(Father):

    def __init__(self, lastName,firstname ,Ffathername, GfirstName):
        super().__init__(lastName,Ffathername,GfirstName)
        self.SfirstName = firstname

    def Sname(self):
        print(self.SfirstName, self.lastName)

son = Son("deshpande","chinmay","shirish","manohar") # function constructor

son.Gname()
son.Fname()
son.Sname()

# single inheritance

class Mother(object):

    def __init__(self,lastName,Mfirstname):
        self.Mfirstname = Mfirstname
        self.lastName = lastName

    def displayName(self):
        print(self.Mfirstname,self.lastName)


class Son(Mother):

    def __init__(self, lastName, Mfirstname,sfirstName):
        super().__init__(lastName,Mfirstname,)
        self.sfirstName = sfirstName


    def displayName(self):
        print(self.sfirstName, self.lastName)
        super().displayName()

class Daughter(Mother):

    def __init__(self, lastName, Mfirstname,dfirstName):
        super().__init__(lastName,Mfirstname,)
        self.dfirstName = dfirstName

    def displayName(self):
        print(self.dfirstName, self.lastName)
        super().displayName()
print('****************')
chinmay = Son('deshpande','kanchan','chinmay')
chinmay.displayName()
gauri = Daughter('deshpande','kanchan','gauri')
gauri.displayName()
kanchan = Mother('deshpande','Kanchan')
kanchan.displayName()

# Multiple inheritance

class Maternal(object):
    def __init__(self,lastname):

        self.lastname =lastname
        print(self.lastname,"maternal")


class Inlaws(object):
    def __init__(self,lastname):
        self.lastname = lastname
        print(self.lastname, "inlaws")

class Son(Maternal,Inlaws):
    def __init__(self,lastName ,firstName):
        super().__init__(lastName)
        self.firstName = firstName

    def displayName(self):
        print(self.firstName,self.lastname)


s = Son("deshmukh",'chinmay')
s.displayName()






















class Inlaws(object):
    def __init__(self,lastname):
        self.lastname = lastname
        print(self.lastname, "inlaws")

class Son(Maternal,Inlaws):
    def __init__(self,lastName ,firstName):
        super().__init__(lastName)
        self.firstName = firstName

    def displayName(self):
        print(self.firstName,self.lastname)


s = Son("deshmukh",'chinmay')
s.displayName()




















