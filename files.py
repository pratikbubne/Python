


#text file

#binary images

#csv

#json


# f = open('hello.txt','w')   # open('filename','mode')
# f.write("Hello")
# f.close()


# f = open('hello.txt','r')
# # r = f.read()
# # print(r)
# # print(f.read())
# print(f.read(3)) # 1 byte
# f.close()




# file w ---- hello

# file  w  --- chinmay



# Performing the write operation on the file


# f = open('hello.txt','w')   # open('filename','mode')
# f.write("Chinmay")
# f.close()


f = open('hello.txt','a')   # open('filename','mode')
f.write("Deshpande" + " ")
f.close()


# Names  exist-

# f = open('names.txt','w+')
# str = input('Please Enter the name of your choice and click on exist to skip')
#
# while "exist" != 'exist':
#     f.write(str + "\n")
#     str = input('Please Enter the name of your choice and click on exist to skip')
#
# f.close()
#
# f = open('names.txt','r')
# for line in f:
#     print(line)
# f.close()

# f = open('names.txt','w+')
# str = input('Please Enter the name of your choice and click on exist to skip')
#
# while str != 'exist':
#     f.write(str + "\n")
#     str = input('Please Enter the name of your choice and click on exist to skip')
#
# f.close()

# f = open('names.txt','r')
# # print(f.readline()) # string
# lines = f.readlines() # list + \n
# for line in lines:
#     print(line)
#



# count of lines
# count of words
# count of charcter


f = open('names.txt','r')

cl = 0
cw = 0
cc = 0

for line in f :
    #print(line) # string
    cl = cl + 1
    cw = cw + len(line.split(" "))
    cc = cc + len(line)

print(f'The number of character is {cc}')
print(f'The number of words is {cw}')
print(f'The number of lines is {cl}')

f.close()
print(len("i am new to python"))











# name = "chinmay"
# print(type(name))



#
# class Person(object):
#
#     def __init__(self,filename,mode):
#         self.filename = filename
#         self.mode = mode
#
#     def write(self):
#         print('Write')
#
#     def read(self):
#         print('read')
#
#
# f = Person('hello.txt','w')
# f.read()
# f.write()
#














