# data structure
# -- string int float
# Collection - dict set tuple list
# user defined - class
# class - Encapsulation , Polymorphism ,Inheritance , Abstractio
# files --
# Exception handling

# Compile time error , Run time Error , Logical errors


#program 1

#compile time error

# if True
#     print('Hello')

# Run time errors // program halt
# print(7/0)


# logical error
# def Sal(amount):
#     return amount * .10 + amount
#
# Sal()



# Exception handling ??


# print('Hello')
# num = int(input('Please enter the value one'))
# num2 = int(input('Please enter the value one'))
# print(num+num2)
# print('This is important line which need to be print on console')



# Run time error examples

#
# h = [1,2,3,4]
# for i in range(5):
#     print(h[i])

# Run time error

# f = open('hello.txt','w')
# num = int(input('Please enter the value one'))
# num2 = int(input('Please enter the value one'))
# f.write(num + num2)
# f.close()


#print("hello"+3)


# if  try should followed with else block
# try:
#     pass
# except Exception:
#     pass
# except Exception:
#     pass
# else:
#     print('')
#
# finally:
#     pass

# finally and else are optional

# 12 / 0 : Arthimetic exception
# str + int  Type error
# Name erroe
try:
    f = open('hello2.txt','w')
    num = int(input('Please enter the value one'))
    num2 = int(input('Please enter the value one'))
    #f.write(2) #2 '2'
    f.write(str(num / num2))
except ZeroDivisionError:
    print('Please donot use 0 in division ')
    try:
        num = int(input('Please enter the value one'))
        num2 = int(input('Please enter the value one'))
        f.write(str(num / num2))
    except ZeroDivisionError:
        print('Please learn Mathematics, chances are over')


except TypeError:
    print('Please Enter the correct input')

else:
    print('Hello')


finally:
    print('Finally always executes')
    f.close()


# Email the email
# 7709192441 - correct msg

#----
# 500 ----
# BaseException
# Exception
#

class MyException(Exception):
    def _init_(self,msg):
        self.msg = msg

accouts = {'chinmay':4400,'shusmita':50000,'pratik':100000}
def belowFive(dict):
    for key , val in dict.items():
        if val < 500:
            raise MyException('Balance cannot be below 500')
try:
    belowFive(accouts)

except MyException as e:
    print(e)

except Exception as e:
    print(e)

else:
    print('All bal are fine')
finally:
    print("happy ending'")

# Regular expression