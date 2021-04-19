#
#
# x = 10
# y = 20
#
# x = "chinmay"
#
# #print(x+y)  # chinmay20
#
# # strongly
# #----------------------------------
#
# a = 10
# b = 20
# print(a+b)
#
# print(type(a))
# print(type(b))
#
# b = "kanchan"
# print(type(b))
#
# d = True
# print(type(d))
#
# c = "chinmay"
# print(type(c))
#
#
# # function
#
#
# x = 10
# y = 20
#
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
#
#
#
# w = 67
# t = 69
# print(w+t)
# print(w-t)
# print(w*t)
# print(w/t)
#
# # DRY
#
# # def functionName(parameter,parameter2):
# #     #statements 1
# #     # statements 1
# #     # statements 1
# #
# # functionName(10,20)
#
#
# d = 34
# c = 56
#
#
# # def calculator(x,y):
# #
# #     x = 35
# #     print(x)
# #     print(x + y)
# #     print(x - y)
# #     print(x * y)
# #     print(x / y)
# #
# #
# # calculator(12,13)
# # calculator(d,c)
# #
# # print(d)
#
# # b = 40
# # m = 90
# #
#
#
#
# # def sub(y,z):
# #     print(z) #  90
# #     z = 48  #
# #     print(y-z) # -8
# #
# # sub(b,m)
# # print(b) # 40
#
#
# # functions
#
#
# #function with no paramter and with no return
#
#
#
# # def add():
# #     print(3+5)
# #
# #
# # add()
# # add()
# # add()
# # add()
# #
#
#
# #function with paramter and without  return type
#
#
# # def add(x,y):
# #     print(x+y)
# #
# # add(12,13) # 25
# # add(50,90) # 140
#
# # function with paramter and with return type
# def add(x,y):
#     return x+y
#
# c = add(35,36)
# print(c + 45)
# print(c-10)
#
# # function without paramter and with return type
#
# def pival():
#     return 3.14
#
# b = pival()
# print(b)
#
#
#
# n = print('hello')
# print(n)
#
#
# t = type(x)
# print(t)
#
#
# name = "chinmay"
# c = name.upper()
# print(c)
#
# # function perform  and it returns
# # string
#
# print('Hello')
#
# name = "chinmay"
# print(type(name))
#
# print('Hello i am chinmay')
# print("Hello i  am chinmay")
# print('chinmay\'s book')
# print("chinmay's  ")
# print("""chinmay's deshpande""")
# print('''chinmay 's book''')
# print(' "New to python " ')
#
#
#
# name = "chinmay"
# lastName = "Deshpande"
# print(name+lastName) # String concatenation
# print(f'My first is {name} and my last name is {lastName}')
# print("My first name is {} and my Lastname is {}".format(name,lastName))
#
#
#
# # Methods
#
# name = "chinmay"
#
#
# #Function performs some action
# #Functions return the value
#
#
#
# def calculator(x,y): # parameter
#     return x + y
# c = calculator(12,13)  # arguments
# print(type(c))
# print(c)
#
#
#
# name = "chinmay"
# c = type(name)
# print(c)
#
#
# x = print('Hello')
# print(x)
#
#
# def  add(x,y):
#     print(x+y)
# x = add(23,34)
# print(x)
#
#
#
#
# name = "rahul"
# print(name[0])
# print(name[1])
# print(name[-1])
#
# #    0    1     2     3    4
# #   R    A     H     U    L
#                          # -1
#
#
# #stringName[start:end:steps]
# # End is not inclusive
#
#
# name = "ChinmayD"
# print(name[1:4]) # hin
# print(name[:5])   # chinm
# print(name[:]) #  As it is
# print(name[0:]) #ChinmayD
# print(name[2:-2])
# print(name[-5:-2])
# print(name[-2:-5]) # End point shoudl always  be forward
# print(name[-5:5])
#
# name2 = "Chinmay Deshpande"
# print(name2[1:16:1])
# print(name2[1:16:2])
#
# print(name2[::1])
# print(name2[::2])
# print(name2[::-1])
#
#
# #  1 - 100
#
# print(1)
# print(2)
# print(3)
# print(4)
#
#
# name = 'pratik'
# print(name[0]) # p
#
#
# # using the first loop
#
# for x in name:
#     print(x)
#
#
# name3 = "pranay"
# for a in name3:
#     print(a)
#
# # looping using range function
#
# name4 = 'jinendra'
# print(name4[0])
# print(len(name4))
#
# for x in range(4):
#     print(x)
#
# for x in range(1,4):
#     print(x)
#
# for x in range(1,5,2):
#     print(x)
#
# for x in range(len(name4)):
#     print(name4[x])
#
# print('**************')
# name5 = "pratik"
# #print(name5[0])
# for y in range(1,6):
#     print(name5[y])
#
#
#
# # slicing
#
# # loops (for and using range fucntion)
# # len() - givens the length of string
# # slcing (string[start:stop:steps])
#
#
#
#
# # # string
# #
# # # upper converts the every character of the string into the upper method
# # name = "chinmayc"
# # x =name.upper()
# # print(x.lower())
# # print(type(x))
# #
# # # lower converts the every character of the string into the upper method
# # c = name.lower()
# #
# #
# # # count the number of character passed to function in the string
# # b = c.count('c')
# # print(b)
# # print(type(b))
# # print("poorva".lower().upper().count('o')) # function chaining
# #
# #
# # # format
# # print("My name is {}".format("chinmay"))
# # print(type("My name is chinmay {}".format(3)))
#
#
# # upper() , lowee(), count(), format()
#
# name6 = "poorva"
# b = name6.capitalize()
# print(b)
#
#
# # gives the index of the character passed to method
#
# n = name6.index('r') # overloaded
# print(n)
#
#
# # match the starting of the string and return the Boolean value if found
# t = name6.startswith('po')
# print(t)
#
#
# # match the ending point  of the string and return the Boolean value if found
# u = name6.endswith('ya')
# print(u)
#
#
# name7 = " chinmay "
# print(len(name7))
# n = name7.strip()
# print(len(n))
# print(n)
#
#
# x = name7.lstrip()
# print(len(x))
# print(x)
#
# s = name7.rstrip()
# print(len(s))
#
#
# # The swapcase changes the upper case letter to the lower and lower case letter to upper
#
# c = "Welcome to python"
# y = c.swapcase()
# print(y)
#
#
# c = y.swapcase()
# print(c)
#
# # title() ... Captilise first char of every word
#
#
# c = "New to python"
# y = c.title()
# print(y)
#
#
# d = "deshpande"
# print(d.capitalize())
#
# #String Testting methods   # Boolean ---- True or False
#
#
# nameNumber  = "Chinmay7709192441"   # Either number or alphabets -- 'special' characters not allowed
# c = nameNumber.isalnum()
# print(c)
#
#
# c = "Chinnmay"  # Only alphabets
# f = c.isalpha()
# print(f)
#
# c = "233A4"
# f = c.isnumeric()
# print(f)
#
#
# # b = input("Please Enter your phone number")
# # if b.isnumeric():
# #         print('Added to database')
# # else:
# #     print('Please Enter the valid number')
#
#
# # a = int(input('Please Enter num 1'))
# # b = int(input('Please Enter num 2'))
# # print(a+b)
#
#
# # ram = input('Please Enter you name')
# # print(type(ram))
#
#
# #0 1 2 3 4 5 6 7 8 9
#
#
#
# #Digits  ??  0 to 9
#
# print('10A'.isdigit())
# print('10A'.isnumeric())
#
#
# # language testing
#
# print('一二三四五'.isnumeric())
# print('一二三四五'.isdigit())
# print('00000'.isdigit())
#
#
# # To check wehther the string is emepty
# print(" A".isspace())
#
#
#
# print("CHINMAY".isupper())
# print("chinmay".islower())
#
#
# # Enter the name   # a = chinmay
# #
# # if a.isupper():
# #     print('store')
# #
# # else:
# #     a.upper()
# #     print('Store')
#
# # x = "LOVE
# #
# # x[::-1]
#
#
#
#
# "I LOVE PYTHON"
#
# c = "I LOVE PYTHON".split(" ")
# print(c)
# stringC = " "
# for word in c :
#     stringC = stringC + word[::-1]+" "
#     print(stringC)
#
# print(stringC.lstrip())
#
#
# # ---------------------------
# print("CHINMAY".replace('C','N'))
# print("POORVA".replace('O','I',1))  #['Character to be replcaed','To be replaced with','Count']
#
#
#
#
# #print("Chinmat".sorted())
#
# # v = "URVASHI"      #  ["U","A]   # SORTED
# # b = []
# #
# # for char in v:
# #    b.append(char)
# #
# # print(b)
# #
# # b.sort()
# # print(b)  # ["A","H"]
# #
# # newString = ""
# # for char in b:
# #     newString = newString+char
# # print(newString)
# #
#
# # -----------------------------
#
# #
# # l = [apple]
# # l.append('apple')
# # a.appen('banana')
# #
#
#
#
#
# # Str = []
# # n = int(input('How many fruits you wanted to sort')) # 5
# # for item in range(n):
# #     fruit = input('Please Enter the fruit name')
# #     Str.append(fruit)
# #
# # Str.sort()
# #
# # for item in Str:
# #     print(item)
#
#
#
#
# # a = "Chinmay Mayuri Nikita Urvashi Sharddha"
# # listA = a.split(" ")
# # userInput = input('Enter the name you wish to search')
# # for item in listA:
# #     if item == userInput:
# #         print('search found')
# #     else:
# #         print('Not found')
#
#
#
#
#
# # a = "chinmay nikita urvahsi ram ravi".split(" ")
# # print(a)
# # #[chinmay,nikita,urvashi,ram,ravi]
# # v = input('please enter string to search') # ravi
# # for item in a:
# #     if item == v:
# #         print('user found ')
# #     else:
# #         print('user not found')
#
#
# # Flag
#
# # a = "chinmay nikita urvahsi ram ravi".split(" ")
# #
# # userFound = False
# # print(a)
# # #[chinmay,nikita,urvashi,ram,ravi]
# # v = input('please enter string to search') # ravi
# # for item in a:
# #     if item == v:
# #         print('user found ')
# #         userFound = True
# #
# # if userFound == False:
# #     print('user not found')
#
#
# #  Logical # A , B , C , D , E , A , A
#
# emptyList = []
# n = int(input('Please enter the 5 names')) # 5
# for item in range(n):
#     name = input('Enter names')
#     emptyList.append(name)
#
# usersearch = input('Name you wish to search')
# print(emptyList)
#
# for item in range(len(emptyList)):
#     if  emptyList[item] == usersearch:
#         print('Find at  {}'.format(item + 1))








#
#
#
# # name = "chinmay"
# #
# #
# # for ch in range(len(name)):
# #     print(ch)
# #     print(name[0])
#
#
#
#
#
#
#
#
#  # AMIT RAM AMIT RAM SHLOK
# #['AMIT', 'RAM' ,'AMIT' ,'RAM' ,'SHLOK']
# #  0        1        2     3      4
#
#
# #
# #
# #
# #
# #
# #
# #
# ## # AMIT 4
#
#
#
# # in keyword
#
#
# if "C" in "Chinmay":
#     print('chinmay')
#
#
#
#
# print("P" in "Pratik")
#
#
# person = {
#
#         'name':'chinmay',
#         'age':30,
#         'language':'English'
#
# }
#
#
#
# for key in person.keys():
#     print(key)
# for jinendra in person.values():
#     print(jinendra)
# for key , value in person.items():
#     print(key ,value)
#
#
#
# # count the number of char form the dict
#
# name = "book"
# emo = {}
# for char in name:
#
#     emo[char] = emo.get(char,0) +1
#
# print(emo)
#
# #--------------------------------
#
#
#
#
# person = {
#
#         'name':88,
#         'age':23
# }
#
#
# person.update(name='chinmay',age=34)
# print(person)
#
# person.pop('name')
# person.popitem()
#

#person.setdefault('k',0)
# f = {}
# name = "book"
# for char in name:
#     f.setdefault(char,0)
# print(f)

#print(dict.fromkeys(['person','name','age'],0))
#tuple / set













