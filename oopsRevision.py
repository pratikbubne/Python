class Student:
    def __init__(self):

        # instance variable
        self.name  = "vishnu"
        self.age = 20
        self.marks = 900

    # this can be an instance method

    def talk(self):
        print('Hi I am ',self.name)
        print('My age is',self.age)
        print('My marks are',self.marks)

s1 = Student()
s1.talk()

# program 2
class Student:
    # this is a constructor

    def __init__(self, n = ' ',m=0):
        self.name = n
        self.marks = m

    def display(self):
        print('Hi ',self.name)
        print('Your marks',self.marks)

s = Student()
s.display()
print('----------------------')

s = Student("jinendra", 800)
s.display()

# program 3


class Sample:
    # this is a function constructor
    def __init__(self):
        self.x = 10  # instance variable

    # instance method
    def modify(self):
        self.x += 1
# create a 2 instances
s1 = Sample()
s2 = Sample()


print('x in s1 =',s1.x)  # 10
s1.modify()
print('x in s1 =',s2.x) # 10
print('x in s1 =',s1.x) # 11

# program 4 class variables


class Sample:
    # this is a class var
    x = 10
    # this is a class method
    @classmethod
    def modify(cls):
        cls.x += 1

s1 = Sample()
s2 = Sample()
s3 = Sample()
print('x in s1 =',s1.x) #10
print('x in s1 =',s2.x)# 10

s1.x = 20
print('x in s1 =',s1.x) #10


Sample.modify()
print('x in s1 =',s2.x) # 11
print('x in s1 =',s1.x) # 20
print('x in s1 =',s3.x) # 20


# program 5

class students:

    # this is a constructor

    def __init__(self,n = '',m= 0):
        self.name = n
        self.marks = m

    # this is an instance method

    def display(self):
        print('Hi',self.name)
        print('Your marks',self.marks)

    def calculate(self):
        if(self.marks >= 600):
            print('you got the first grade')
        elif(self.marks >= 500 and self.marks < 600):
            print('You got second grade')
        elif(self.marks >= 350):
            print('you got the third grade')
        else:
            print('Please try again')

i = 0

while(i < 2):
    name = input('Please Enter your name ')
    marks = int(input('Please Enter the marks'))
    s1 = students(name,marks)
    s1.display()
    s1.calculate()
    i += 1
    print('-----------------')



# coin tossed?? // while
# 3 coin   for -- definite of times for

# program 6 :

class Student(object):

    # mutator method  (setter)
    def setName(self,name):
        self.name = name

    # accessor  (getter)
    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    # accessor  (getter)
    def getMarks(self,):
        return self.marks

for item in range(2):
    name = input('Please Enter your name ')
    marks = int(input('Please Enter the marks'))
    s1 = Student()
    s1.setMarks(marks)
    print(s1.getMarks())
    print('-----------------')
    s1.setName(name)
    print(s1.getName())



























