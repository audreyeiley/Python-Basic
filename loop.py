# for variable in range(start, end, step) :
#   code to loop

# range(start, end, step) where start, end, step are numbers [ ex. range(1, 5, 2)]
# From start to end-1(end not included) put the increased/decreased value step by step into a variable and loop.
# Don't necessarily have to enter the start and step.
# If start is not entered, 0
# If step is not entered, 1
# range(5)  => Start and step not entered
# range(0, 5, 1)    => step not entered
# range(0, 5, 1)    => standard


# for i in range(0, 5, 1) : # repeats 5 times with i taking values 0,1,2,3,4 
#     print(i)

# for i in range(0, 5, 1) :
#     print('Hello')  # do not use variable in the repeated code



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# problem : print odd number from 1-100 
# for i in range(1,101, 2) :  # 1, 3, 5, 7 ...97, 99, 101
#                             # add 2 and than it will become odd
#     print(i)

# problem : print multiples of 5 from 5 to 100
# for i in range (5, 101, 5) :
#     print(i)

# problem : print perfect squares up to 10000 (print x*x)
for i in range (1,101, 1 ) :
    print(i*i)      # the answer is in the question, or the problem since x is not a variable use the variable as i.



    