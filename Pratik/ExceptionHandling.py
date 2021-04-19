# Compile time error , Run time Error , Logical errors

# Compile Time Error

# SyntaxError
# num = int(input("Enter the number:"))
# if num%2 == 0                                    #SyntaxError: invalid syntax
#     print('You have entered an even number.')
# else:
#     print ('You have entered an odd number.')


# Run Time Error  ------- program halt

# ZeroDivisionError
# num1 = int(input('Enter a First number: '))   #23
# num2 = int(input('Enter a Second number: '))  #0
# result = num1/num2                            #ZeroDivisionError: division by zero
# print (num1,'divided by',num2,'equals: ',result)

# file = open('Runtimeerror.txt','w')
# num1 = int(input('Please enter the value One: '))  #10
# num2 = int(input('Please enter the value Two: '))  #pratik
# file.write(num1 + num2)                            #ValueError: invalid literal for int() with base 10: 'pratik'
# file.close()


# Logical Errors
# IndexError
# New = [1,2,3,4,5,6,7,8,9]
# for i in range(len(New)+1):            #IndexError: list index out of range
#     print(New[i])

# try and except
# if  try should followed with else block

# try:
#     pass
# except Exception:
#     pass
# except Exception:
#     pass
# else:                         # Optional
#     print('')
# finally:                      # Optional Execute always
#     pass

# try:
#     file = open('Runtimeerror.txt','w')
#     num1 = int(input('Please enter the value One: '))  #10
#     num2 = int(input('Please enter the value Two: '))  #pratik
#     file.write(num1 / num2)                          # 
#     file.write(str(num1 / num2))                           
#     file.close()  
    
# except ZeroDivisionError:
#     print('Please donot use 0 in division ')

# except TypeError:
#     print('Please Enter the correct input')

# else:
#     print('Hello')

# finally:
#     print('Finally always executes')
#     file.close()

# try and except Nested
# try:
#     file = open('Runtimeerror.txt','w')
#     num1 = int(input('Please enter the value One: '))  #10
#     num2 = int(input('Please enter the value Two: '))  #pratik
#     file.write(num1 / num2)                          # 
#     file.write(str(num1 / num2))                           
#     file.close()  
    
# except ZeroDivisionError:
#     print('Please donot use 0 in division ')
#     try:
#         file = open('Runtimeerror.txt','w')
#         num1 = int(input('Please enter the value One: '))  #10
#         num2 = int(input('Please enter the value Two: '))  #pratik
#         file.write(num1 / num2)                          # 
#         file.write(str(num1 / num2))                           
#         file.close() 
#     except ZeroDivisionError:
#         print('Please learn Mathematics, chances are over')

# except TypeError:
#     print('Please Enter the correct input')

# else:
#     print('Hello')

# finally:
#     print('Finally always executes')
#     file.close()

# User Define Exception
# class MyException(Exception):
#     def _init_(self,msg):
#         self.msg = msg

# accouts = {'Pratik':2000,'Prasad':3000,'Pravin':100000}
# def belowFive(dict):
#     for key, val in dict.items():
#         if val < 500:
#             raise MyException('Balance cannot be below 500')
# try:
#     belowFive(accouts)

# except MyException as e:
#     print(e)

# except Exception as e:
#     print(e)
# else:
#     print('All bal are fine')
# finally:
#     print("happy ending'")
