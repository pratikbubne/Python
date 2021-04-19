# decorator

# Anonymous function

# map reduce filter//


# def square(x):
#     print('Hello i am new to python ')
#     print('hello I am learning javascript')
#     print('Helloooooo new to concept')
#     return x * x
#
# square(2)


# f = lambda  x:x*x
# print(f(2))
# def max(x,y):
#     if x > y:
#         print(x)
#     else:
#         print(y)

# max(12,14)
#
# y = lambda x,y:x if x > y else y
# print(y(10,3))
#
# r = lambda x,y:x+y
# print(r(10,20))
# #--------------------------
#
# 12,13
# a,b =[int(n) for n in input('Enter the number').split(',')]
# print(f'Bigger number is {y(a,b)}')

# 12,13


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

listA= [12,14,4,55,5516]
#[True,True,True,False,True]
# listB = []
# for item in listA:
#     listB.append(is_even(item))
# print(listB)
# h = list(filter(is_even,listA))
# print(h)



# h = list(filter(lambda x:(x%2  == 0),listA))
# print(h)


#
# h = list(map(lambda x:x+10,listA))
# print(h)
#
# r = tuple(map(lambda y:y*y,x))
# print(r)


import functools
from functools import reduce
x = [3,3,4,5,6,7]
y = functools.reduce(lambda z,y:z+y,x)
print(y)

k = [1,2,3,4,5,6,7]
j = [1,3,4,5,6,6,7]


y = list(map(lambda x,y:x*y,k,j))
print(y)

# generator


# x = [12,13,14,14]
#
# def sqt(lst):
#     f = []
#     for item in lst:
#         f.append(item * item)
#
#     return f
#


# ////  genrators ---- loop




listA =  ["apple","banana","cheery"]
u = iter(listA)
# print(next(u))
# print(next(u))
# print(next(u))
# print(next(u))
for i in listA:
    print(i)

# Generators-------->
# Date -- Django --- date import