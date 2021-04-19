

# set and dict are similar

a = {1,2,3,4,5,6,1,1,3,4}
print(a)
print(type(a))


#no slice
#print(a[::-1])


# set does not stores the value by index
# normal loop with out range fucntion

# for item in a:
#     print(item)

# for item in range(len(a)):
#     print(a[item])

#print(a[0])

print(len(a))
print(sorted(a))

print(min(a))
print(max(a))
#print(del a)
print(sum(a))
#print(list(reversed(a))) with not work -- sum iterable , which stores the value by index


a = {1,2,3,4,5}
b = {6,7,8,9,10}


# Method performs some action and methods return some data


# ab = a.pop()
# print(ab)
# print(a)

# a.clear()
# print(a)


# a.update(b)
# print(a)

b.update([99,100,102])
print(b)

# update() , iterable as a paramter  (which stores the value by -- string list tuple )



t = a.copy()
print(type(t))
print(t)


# a.remove(7)
# print(a)


# to add the element into the ser

a.add(5)
print(a)

d = a.union(b)
print(d)






n = {"A","B","C"}
m = {"E"}

print("***************")
print(n.isdisjoint(m)) # return true when the set have different set of values
print("***************")

#m.remove('V')
# m.discard("N")


#
# m.discard("B")
# print(m)


print(n.symmetric_difference(m))
n.symmetric_difference_update(m)
print(n)

print("*****")






# set -

abc = {"A","B","C"}
nvb = {"A","E","F"}

# is -- booolean

n = {"A","B","C"}
m = {"A","B","C","D"}

print(n.issubset(m))
print(m.issuperset(n))




print(abc.issuperset(nvb))
print(abc.issubset(nvb))


# print(abc.union(nvb))




# c = abc.intersection(nvb)
# print(c)
# print(abc)
#
# abc.intersection_update(nvb)
# print(abc)

# nvb.intersection_update(abc)
# print(nvb)


# b = abc.difference(nvb)
# b = nvb.difference(abc)
# print(b)
#
#
# abc.difference_update(nvb)
# print(abc)
#
# nvb.difference_update(abc)
# print(nvb)



# Stri











