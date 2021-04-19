
tupleA = ("A","B","C")
print(tupleA)

listA = list(tupleA)
print(listA)
print(type(listA))


listB = [1,3,4,5,6,7]
y = tuple(listB)
print(y)


setB = {1,3,4,5,6,8}
listC = list(setB)
print(listC)


dictA = {

    'name':"chinmay",
    'age':34

}
c = list(dictA)
print(c)


listD = ['name','age','rollNum']
print(dict(listD))