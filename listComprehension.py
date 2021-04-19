#
#
# #1 4 9
#
# #[1,4,9,16,25,36,49,64,81,100]
#
# # squares = []
# # for item in range(1,11):
# #     squares.append((item*item))
# # print(squares)
#
# #List comprehension --- list
#
# #"A B C D E F G H".split()
#
# # program 1
#
# # squares = [(item * item) for item in range(1,11)]
# # print(squares)
#
# #program 2
#
#
# # List comprehension syntax
# # [
# #     expression for item in iterable if statement
# #
# # ]
#
# # evenSqaures =[(item * item)for item in range(1,11) if item % 2 == 0]
# # print(evenSqaures)
# #
# #
# # #program3
# #
# x = [10,20,30,40]
# y = [20,40,55,66]
#
# #[30,60,85,106]
#
# lst = []
#
# for item1 in x:
#     for item2 in y:
#         lst.append(item1+item2)
# print(lst)
#
# lst =[(item1 + item2)for item1 in x for item2 in y]
# print(lst)
#
# blank = []
# for item in range(len(x)):
#     blank.append(x[item]+y[item])
# print(blank)
#
# additonOnIndex = [x[item]+y[item]for item in range(len(x))]
# print(additonOnIndex)
#
#
# fruits = ['Apple','Banana','Grapes','Mango']
#
# #['A','B','G','M']
#
# blank2 = []
# for item in fruits:
#     blank2.append(item[0])
# print(blank2)
#
# newlist = [item[0] for item in fruits]
# print(newlist)
#
#
# num1 = [1,2,3,4,5]
# num2 = [10,11,1,2]

# [3,4,5]
#[10,11]
# bnk = []
# for item in num1:
#     if item not in num2:
#         bnk.append(item)
# print(bnk )
# bnk = []

# for item in num2:
#     if item not in num1:
#         bnk.append(item)
# print(bnk)

# newlist = [item for item in num1 if item not in num2]
# print(newlist)


# input()  ---- string
# eval() ------ ??


# a = input('Please do addition of two numer')
# print(a)


# b = eval(input('Please do addition of two numer'))
# print(type(b))
# print(b)

#-----------------------------------------------------------


def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


# Driver code
lst = ['a', 1, 'b', 2, 'c', 3]
dictA = {lst[i]:lst[i+1] for i in range(0,len(lst),2)}
print(dictA)


# Not possible

# tupleA = ('a', 1, 'b', 2, 'c', 3)
# dictA = (lst[i]:lst[i+1] for i in range(0,len(lst),2))
# print(dictA)




# j = {
#     'a':1,
#     'b':2,
#     'c':3
# }
#




















# print(Convert(lst))

















