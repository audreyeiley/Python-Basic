# variable = ["value," value]   =. The data type of the value does not matter 
# use i the above form
# list is a collection of multiple data types in order in one variable 
# The order of values starts from 0 => It is called the index number 
# When bringing the values, refer to them using []

# list1 = {1, 'cit', True} 
# print(list)
# print(list1[0]) # Get list1 index number 0 value
# print(list1[2])
# print(list1[3]) # Get list1 index number 3 value. There is a index number 3, so an error occurs.



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# you can use the index number to modify the value at that index number
# changing the value can be done as if saving the value in a variable
# a = [1, 'cit', True]
# print(a)

# a[1] = "hello"  # Change the value of the index number 1 of a.
# print(a)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# list1 = ["abc", "dfg", "hij", 123, 456]
# print(list1)
# print()

# print("Q1. change the 1st element of list1 to 'park'.")
# list1[1] = 'park'
# print(list1)
# print()

# print("Q2. Name the variable arr ad save the list below. [4,8,12,16,20,24,28,32] ")
# arr = [4,8,12,16,20,24,28,32] 
# print(arr)
# print()

# print("Q3.Change the 4th element of arr to 'cit ")
# arr[4] = 'cit' 
# print(arr)
# print()

# print("Q4. Run print(list1) and print(arr)")
# print(list1)
# print(arr)
# print()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


for i in range(1, 9, 2):
    print(i)
print()

list1 = [1,3,5,7]
for i in list1:     #can insert a list variable instead of range
    print(1)        # Get the elements of a list one by one 
print()

list2 = ['a','hello','cit', 'codng', 'A' ]
for j in list2 :
    print(j)
print()
