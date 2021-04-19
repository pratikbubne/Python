#
#
# # Strings stores the value by index
#
# name = "chinmay"
# print(name[0])
#
# for char in name:
#     print(char)
#
# for char in range(7):
#     print(char)
#     # 0 ,1,2,3,4,5,6
#     print(name[char])
#
#
#
#
#
# print(type(name))
#
# # list ---> multiple elements
#
# # List stores the value by index
#
# a = "Apple"
# b = "Mango"
# c = "Bananna"
# print(a,b,c)
#
# # List
#
# fruits = ["Apple","Mango","Banana" "Chiku","Papaya","Grapes"]
# print(fruits[0])
#
# for fruit in fruits:
#     print(fruit)
#
# print('**************************')
#
# for fruit in range(len(fruits)):
#     print(fruits[fruit])
#
# print(fruits[0:2])  # [start:end(not inclusive):step]
# print("Apple" in fruits)
#
#
# # ---------------------------------------
#
#
# userInput = input('Please Enter the fruit you want to buy')
# # for item in fruits:
# #     if item ==  userInput :
# #         print('Fruit available ')
# #     else:
# #         print('Not available')
#
#
# # if userInput in fruits:
# #     print('Fruit available')
# # else:
# #     print("Not available")
#
#
# # len
#
# print(len(fruits))

#--------------------------------------------------

# Methods of list


car = ["BMW","AUDI","PORSCHE","MARUTI","TATA"]


# index

print(car.index("AUDI"))

# append
car.append("HYUDAI")
print(car)

# pop with parameter  and pop with parameter


c = car.pop()
print(c)
print(car)

car.pop(2)
print(car)



car.sort()
print(car)


print(car.count("AUDI"))

car.extend(["NEW1","NEW2"])  # LIST
car.extend("CHINMAY")        # STRING
car.extend(("NINAD","CHINMAY")) # TUPLE
print(car)



# reverse
car.reverse()
print(car)


#
car.insert(2,"PORSCHE")
print(car)


# remove

car.remove("MARUTI")
print(car)


car.clear()
print(car)


# del car
# print(car)


n = [1,3,4]
v = n
n[2] = 56

print(n)  #  1,3,56
print(v)  # 1,3,56



grapes = ["A","B","C"]

BAN = grapes
BAN[0] = "BBB"
print(grapes)  # ['BBB',"B","C"]
print(BAN)      #['BBB',"B","C"]


a = [1,2,4]

b = a.copy()


print(a)
print(b)


b[0] = "a"

print(a)
print(b)

a = "hello"

for char in range(len(a)):
    if a[char] == 'l':
        print(a[char] , str(char+1))







