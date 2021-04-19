# name = "A2D3"
# #AADDD
# newString = ""
# for item in name:
#     if item.isalpha():
#         x = item   #x = D
#     else:
#         newString = newString + int(item) * x
# print(newString)

# name = "4D3C"
# #DDDDCCC
# blank = " "
# for char in name:
#     if char.isnumeric():
#         x = int(char)
#     else:
#         blank = blank + char * x
# print(blank)

# name ="A4D3C2"
# # AAAADDDCC
# blank = ""
# for char in name:
#     if char.isalpha():
#         x = char # A #D
#     else:
#         blank =  blank + x * int(char) #AAAADDD
# print(blank)

#name ="4A3D2C"
# #AAAADDDCC
# blank = ""
# for char in name:
#     if char.isnumeric():
#         x = char # A #D
#     else:
#         blank =  blank + int(x) * char #AAAADDD
# print(blank)

# name = "AAAAACCCCDDZ"
# seta = sorted(set(name))
# blank = ""
# for item in seta:
#     a = item + str(name.count(item))
#     blank = blank + a
# print(blank)

# name = "AAAZZZZZIIIIIMMMMMEEEEEUUUUUIIIIIOOOOOOOUUUUU"
# namey = sorted(set(name))
# namec = ["A","E","I","O","U"]
# print(namec)
# for item in namey:
#     if item in namec:
#         print(item,name.count(item))

#sum()

# LEVEL # PALINDROME

# name = "LEVEL"
# rev = name[::-1]
#
# if name == rev:
#     print('print PALINDROME')


#LISTEN  SILENT  ANAGRAMS

name = "LISTEN"
name2  = "SILENT"

setA = set(name)
setB = set(name2)
if len(name) == len(name2):
    if setA == setB:
        print('ANAGRAMS')

# a2h2w3
#achjwz
# ASCII

# "BOOK"
# {B:1}

name = "AAAAACCCCDDZ"

dict = {}

for item in name:
    dict[item] = dict.get(item,0) +1

print(dict)
blank = ""

for k,v in dict.items():
    blank = blank + (k+str(v))

print(blank)

lista= [2001, 2002]
ageNew =[] 
for i in lista:
    age = 2021 - lista[i]
    
#******************************************************
#20/02/2021
# listA = [2002,2000,1998,1997,1996,2008]
# bill = [300,200,500,700,50,700]
# #discount = [30,]
# #[18,20,22,23,24,12]
# #[2012,2010,2008]
# #[354,....]
# def returnList(list,fn):
#     listC = []
#     for item in list:
#         listC.append(fn(item))
#     return listC
#
# def calDicount(el):
#     return 0.10 * el
#
# def calGST(el):
#     return 0.18 * el + el
#
# gstValue = returnList(bill,calGST)
# print(gstValue)
#
# sumDis = returnList(bill,calDicount)
# print(sumDis)
# print((sum(sumDis)/sum(bill)) * 100)
#
# def calculateAge(el):
#     return 2021-el
#
# def addingTen(el):
#     return el + 10

# sum()
# min()
# max()
# sorted()
# reversed()
# len()
# del

# b = returnList(listA,addingTen)
# print(b)
#
# v = returnList(listA,calculateAge)
# print(v)
#

# listB = []
# for item in listA:
#     listB.append(2021-item)
# print(listB)
#
# listC = []
#
# for item in listA:
#     listC.append(item+10)
# print(listC)

a = "AAAADDDCCBQ"
b = set(a)  # b {'A','B','C','D'}

#A4D3C2B1Q1

nma= ""
nm = []
for item in sorted(b):
    print(nm.append(item))
    print(nm.append(str(a.count(item))))
print(nm)

v = "".join(nm)
print(v)

# 
# w = "aeiouabc"
# 
# # AEIOU
# count = 0
# for char in w:
#     char = char.lower()
#     if char == 'a' or char =='e' or char == 'i' or char == 'o' or char == 'u':
#         count = count + 1
# 
# print(count)
# 
# 
# b = 'aieouAEIOU'
# count = 0
# for char in w:
#     if char in b:
#         count = count +1
# 
# print(count)
#
