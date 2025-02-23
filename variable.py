# variable = value
# Save the value in variable in the format above.
# = Unlike the meaning of the symbol, the value is simply stored in a variable.
# Variable can be whatever you want as long as you follow the rules below.
# 1. Impossible to start with a number
# 2. Special characters are not possible except the symbal "_"
# 3. No spacing
# 4. Reserved words not possible

# my_name = "Eiley"  


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

#  Data types 
# str   -> String   -> made up of air quotes " " ' '
# float -> Float    -> no quotes and has a decimal point 
# int   -> Integer  -> no quotes and no decimal point
# Everyday words (English, Chinese, korean, etc.) without quotes => error

# a = 10    # saves the integer 10 in the variable a
# b = 'cit' # saves the string 'cit' in the variable b

# name = 'Eiley'
# age = 11
# Height = 150

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# print('text' or variable or number)
# The print () funtion prints the 'text', number, or value of
# the variable inside the bracket and then adds a newline.
# To print mulitple items, use a comma (,)
# If you print() with nothing inside, it prints an empty line

# name = 'python'
# age = 11
# height = 150
# print(name)
# print()     # prints an empty line
# print(age)
# print(height)
# print('hi')
# print()
# print(5)
# print(5*10)
# print(name, age, height, "hello")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# input('text' or value or variabe)
# Displays 'text' or the value of the variable, then waits for keyboard input until Enter is pressed.
# 'text' or variable can be left out
# variable = input('text' or variable)
# Usually used in this format, without variable it the input value is not saved
# input() always saves the value as a str data type

# var1 = 2
# var2 = input("insert anything : ") 
# print(var2)   
# print(type(var2))

# var2 = int(var2)
# print(type(var2))

# sum = var1 + var2
# print(sum)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# Type casting
# str(variable or value)    => converts variable or value to str data type 
# float(variable or value)  => converts variable or value to float data type 
#int(variable or value) => converts variable or value to int data type
# Just using them in calculations doesn't change the original variable's data type 
# To change the original variable's data type, save it back into the variable ( ex. a = int(a))

# var1 = 2
# var2 = '31'
# result = var1 + int(var2)   # saves var1 + var2 converted to int in result
# print(result)
# print(type(var2))       # Prints the data type of var2 which is str
# var2 = int(var2)        # converts var2 to int and saves it back in var2
# print(type(var2))       # prints the new data type of var2 


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
 
# print('Hello, enter your name.')   
# name = input()      # I have to do this not put var or this # var2 = input("insert anything : ") sadly :(

# print("welcome", name, ", enter your age")  # do this do that
# age = input()
# age = int(age)
# year = 2025 - age

# print("you were born in", year,"! Enter your height.") 
# height = int(input())
# two_m = 200 - height

# print("There are", two_m, "cm left unil 2m" )


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# +     add 
# -     subtract
# *     mulitply 
# /     divide (result is a flock)
# //    integer division (result is a int) 
# %     modulus (remainder)
# **    exponet (power)

# a = 10
# b = 3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)
