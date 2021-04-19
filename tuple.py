


# String , Tuple ,Dict ,
# return
#  String

name = "chinmay"
for char in name:
    print(char)

for char in range(len(name)):
    print(name[char])


# list

listA = ["Bharat","Chinmay"]

for item in listA:
    print(item)


for item in range(len(listA)):
    print(listA[item])


# Dictionaies


person = {
    "name":"chinmay",
    'age':30,
    'language':'English'

}
for key in person.keys():
    print(key)

for values in person.values():
    print(values)

for keys , values in person.items():
    print(keys , values)


# tuple

# list and tuple are similar  (index)

# dictionaries and set (not stored)

# Why is difference between tuple and list

#tuples are immutable


name = ["A","B","C"]
name[2] = "E"
print(name)


man = ("A","B","C","B","B","C")
#man = ("CDE","NINAD","FRF)


print(man[0])
print(man[1])
print(man[2])

for item in man:
    print(item)

for item in range(len(man)):
    print(man[item])

#
a = man.count("A")
print(a)

b = man.index("B",4)
print(b)


a = 1
print(type(a))

b = 1,
print(type(b))

#--------------------------

# passing list as a parameter to  function

a = [1,2,3]
b = ["c","d","e"]

def printList(list):
    for item in list:
        print(item)
    return  list

printList(a)
printList(b)


# passing dict as a parameter to  funtion


person = {

    'name':"chinmay",
    'age':30

}


def printDict(dict):
    for key in dict:
        print(key,dict[key])

    # for key ,val in dict.items():
    #     print(key,val)

printDict(person)



# tuple as a parameter the another function


b = ('A','B','C')


def printTuple(tup):

    for item in tup:
        print(item)

printTuple(b)



# Take value from user and put it in list and print list

# 3 times

def printList(list):
    for item in list:
        print(item)
    return  list


#
# fruits = []
# for x in range(3): #0 1,2
#     userfruit = input('Please enter your fav fruits')
#     fruits.append(userfruit)
# print(fruits)
# s = printList(fruits)
# print(s)


# ---------------------




def dictR(listaaa):
    bdict = {}
    for item in listaaa:
        print(item)
        bdict[item] = "A"

    return bdict


v = dictR(["A","B","C"])
print(v)



def printAdd(x,y):

    print(x+y)
    return (x , y)

a = printAdd(12,13)
print(type(a))
print(a)




a = ("abhisha","mayuri","komal","poorva")

print(a[1:])
print(a[:2:2])
print(a[::-1])


len(a)
del a



listA = [1,2,3,4,5,6,7,8,9]
print(listA[::2])
print(listA[::-1])

len(listA)
del listA


name = "chinmay"
print(name[::-1])

len(name)

del name


ab = {
    'name':'a',
    'age':'b',
    'roll':12
}

print(len(ab))
del ab


print(min([111,2,3,4,5,6,7,]))
print(min((3,4,5,6,78)))

print(max([111,2,3,4,5,6,7,]))
print(max((3,4,5,6,78)))


print(min(["poorva","pooja","ram"]))
print(max(("A","B","C","D","E")))


print(sorted([11,3,4,5]))
print(sorted("ILK"))     # list

#del


#len


# print(sum([1,2,3,4,5,6,7]))
# print(sum((1,2,3,4,5,6,7,8)))
#
# print(sum(['A','B','C']))
# print('A'+'B'+'C')

# reversed tuple list numbers

reversed([1,2,3,4,5,6])
a = list(reversed(["D","R","Y"]))
print(a)

b = ('A','B','C','D')
print(list(reversed(b)))

name = "Chinmay"
print(list(reversed(name)))

y = [1,3,4,5,6,7,8,9]
print(list(reversed(y)))


# "name"

# name= "chinmay"
# print(name[::-1])
# t = list(reversed(name))
#
#
# newString = ""
# for char in t:
#     newString = newString+char
# print(newString)
#
#
# newString = ""
# for char in range(len(name)):
#     print(name[char])
#     newString =  name[char] + newString
# print(newString)


# class Person():
#     age = 10
#     color = "fair"
#
#     def printAge(self):
#         print(self.age, self.color)
#
#
# raju = Person()
# ram = Person()
#
# print(raju.age)
# raju.age = 50
#
# print(ram.age)  # 10
# print(raju.age)  # 50




name = "Rahul"

#steps

print(name[::-1])



newString = ""

for char in name:
    newString = char + newString
print(newString)



name = "Amol"

e = reversed(name)
print(e)

newString = ""

for char in e:
    newString =  newString + char
print(newString)


namer = " "

name = "I am new to python"  # Reverse every word in the string
name = name.split()
for item in name:
    namer = item + " "+ namer

print(namer)


name = "My name is mike"

newlist = []

listA = name.split()
for item in listA:
    newlist.append(item[::-1])
print(newlist)


a = " ".join(newlist)
print(a)
print(type(a))


"AZCD1234"



a = sorted('AZCD1234')
print(a)
print("".join(a))


digit = []
alpha = []

for char in a:
    if char.isalpha():
        alpha.append(char)
    else:
        digit.append(char)


print(digit)
print(alpha)
print("".join(alpha+digit))


name = 'A4B3C2Z1'

newString = ""
#AAAABBBCCZ


# "A"*4
for char in name:
    if char.isalpha():
        x = char #A
    else:
        c = x * int(char)
        newString = newString + c

print(newString)



# 21 days  # 150 alog
#
# 300 API
#
# 150 selenium
#
# cypress
#

#5 logical
















