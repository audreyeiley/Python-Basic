# Comparison operators
# The result of the comparison operation is always True or False
# ==    :   [equal to]
#           True if the same, False if different.

# !=    :   [not equal]
#           True if different, False if the same.

# <     :   [less than]
#           True if the right side is larger (excluding equal values), otherwise return False.

# >     :   [greater than]
#           True if the left side is larger(excluding equal values) otherwise return False

# <=    :   [less than or equal too]
#           True if the right side larger or equal, otherwise return False

# >=    :   [greater than or equal to]
# True if the left side is larger or equal, otherwise return False   

# print(5 !=2)
# print(5 < 2)   

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# if(condition) :
#   Run if the above condition is True
# elif(condition) :
#   Run elif the above condition is True
# else :
#   Run if all condition are false

# if    : always use 1
# elif  : use range 0 - infintity 
# else  : use 0 or 1 
# if can be used by nesting within if.             


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# 160 - 90  :A
# 89 - 70   :B
# 69 - 60   :C
# 59 -      :D

# score = int(input())

# if(100 >= score >= 90) :
#     print('A')
# elif(89 >= score >= 70) :
#     print('B')
# elif( 69 >= score >= 60) :
#     print('C')
# elif(59 >= score >= 0) :
#     print('D')

# print("End")    



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# age = int(input("Enter your age : "))       # This is the right way to and then write condition below

# if(12 <= age) :     # Don't make words make the operators ex. <,> those stuffys and i need to do that so i can tell only above 12 can watch
#     print("Good, have fun watching.")
# if(12 > age) :
#     print("Sorry, only above 12 years old can watch.")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #



# print("Enter number")    # If I wanna make the text below the question make it like this not the one above.
# number = int(input()) 
    
# if(number%2 ==0) :      # write the variable above ex. Number
#     print("Even")
# if(number % 2 != 0) :  # can't divide by 2
#     print("Odd")
    

 
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# not   :if true the result is reveresd to false. If it is false, the result is reversed to true.
# and   : true if both sides are true, false if even one is false 
# or    : False if both sides are false, true if at least one side is true
# The execuation order is executed in the order of not, and, or.

# print(not(1==1))
# print((1 != 5) and (10 <= 15))
# print((6!= 6) or (5 ==3 ))   


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #





# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #




# age =int(input("Enter your age"))
# is_member = input("Are you a member? (Yes or no):")

# if(age >= 18) :
#     if(is_member == "yes") :
#         print("Welcome, Adult member!")
#     else :
#         print("Adult non-member, please sign up.") 
# else :
#     if(is_member == "yes") :
#         print("Welcome young member!") 
#     else :
#         print("Young non-member, please sign up.")
    

