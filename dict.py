




listA = ["manago",'banana',"chiku"]

print(listA[0])
print(listA[-1])
print(type(listA))

# Loop

for item in listA:
    print(item)

for item in range(len(listA)):
    print(item)
    print(listA[item])

listB = ["chinmay","deshpande",14,30]

# dictinary

person = {

        'firstname':'chinmay',
        'lastName':'deshpande',
         'age':12,
         'rollNumber':30

}
# Bracket notation
print(person['firstname'])

# get method of dictionary
print(person.get('lastName'))

for key in person:
    #print(key)
    print(key,person[key])


print(person['firstname'])
person['firstname'] = "ninad"
person['color'] ='black'
#print(person)


# Methods


# clearing the name

# person.clear()
# print(person)


# deleting the data structure
# del person
# print(person)

#

person2 = person.copy()

print(person)
print(person2)
person['firstname'] = "ram"
print(person)
print(person2)


#?


# a = {
#
#     'a':10,
#     'b':11
# }
#
# b = a
# print(type(b))
#
# b['a'] = 200
# print(a)
# print(b)


student = {
    "name":'chinmay',
    "lastname":"deshpande",
    'rollnumber':23,
    'skills':['c','python','javascript','sql','postgres'],
    'age':30,
    'family':{
        'father':'shirish deshpande',
        'mother':'kanchan deshpade',
        'sister':'Gauri deshpande'
    },
    'isMajor':True,
    'school':'ninad',
    'grades':[12,23,34,45455,6,55666]
}


# pop to remove key and values

# print(student.pop('skills'))
# print(student.pop())

print('*************')
print(student.values())
print(student.keys())
print(student.items())
print('*************')



# for a in student.keys():
#     print(a)
#
#
# for a in student.values():
#     print(a)
#
# for k , v in student.items():
#     print(k,v)



# print(sum(student['grades'])/int(len(student['grades'])))
# print(student['age']+ student['rollnumber'])
















# for  key in student:
#     if key == 'family':
#         for keys in student[key]:
#             print("welcome "+student[key][keys])
#
# print(len(student['family']))





















#
# student['skills'].append('cypress')
# print(student)
#
# # Total number of skilss
# print(len(student['skills']))
#
#
#
#
#














# printing all the items skills

# for key in student:
#     if key == 'skills':
#         arr = student[key]
#
#         # for item in arr:
#         #     print(item)
#
#         for item in range(len(arr)):
#             print(item+1,arr[item])













# name = 'chinmay'
# len(name)
# del name
# sorted(name)
#
# listA = ['A','B','C']
# len(listA)
# del listA
# sorted(listA)
#
#
# b = {
#
#     'a':10,
#     'n' :20
# }
#
# len(b)
# del(b)
# sorted(b )








w = "aeiouabc"

# AEIOU
count = 0
for char in w:
    char = char.lower()
    if char == 'a' or char =='e' or char == 'i' or char == 'o' or char == 'u':
        count = count + 1

print(count)


b = 'aieouAEIOU'
count = 0
for char in w:
    if char in b:
        count = count +1

print(count)

