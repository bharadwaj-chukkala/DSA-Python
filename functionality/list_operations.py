'''
This file contains the functions that are used to manipulate the  list
'''

##### Creating a list ########
my_list = []
# or
my_list = list()

##### Add Element to end of list ########
my_list.append('Hello')
print(my_list)

##### List can contain different elements ########
my_list = [1, 2.0, True, 4, 'Hello', 0.006, 'World']
print(my_list)

##### Accessing an Element of the list ########
value = my_list[3]
print(value)


##### 2D list ########
my_list = [['Geeks', 'For'], ['Geeks']]
print(my_list[0][1])


##### Accessing an Element of the list using negative index ########
my_list = [1, 2.0, True, 4, 'Hello', 0.006, 'World']
value = my_list[-2]
print(value)


##### Size of the list ########
size = len(my_list)
print(size)

############################################
######## Advanced List Operations ##########
############################################

##### Taking input and storing in a list ########
# 1. Input as a string

input_string = input("Enter Values you want to add to a list with spaces between the elements")
lst = input_string.split()
print(lst)

# 2. Using the map function
n = int(input('Enter size of list'))
lst = list(map(int, input("Enter the integer elements of the list").strip().split()))[:n]
print(lst)

##### Adding elements using insert to a list ########
my_list = [1, 2.0, True, 4, 'Hello', 0.006, 'World']
print(my_list, " <-- current list")
my_list.insert(2, 456.789)
print(my_list, " <-- after inserting value")


##### Adding multiple elements  to a list using extend ########
my_list.extend([231, 'Drew', 90.33])
print(my_list, " <-- after extending")

##### Creating a copy of a list ########
new_list = my_list.copy()

##### Reversing a list ########
# 1. Using .reverse() method. Reverses the original list without returning value
new_list.reverse()
print(my_list, " <-- original list")
print(new_list, " <-- reversed list")

# 2. Using reversed() function. This returns a value
rev_my_list = list(reversed(my_list))
print(rev_my_list, " <-- reversed list 2.0")

##### Removing occurence of an element in a list ########
my_list.remove("Hello")
print(my_list, " <-- Removed first occurence of Hello")

del my_list[0]

print(my_list, " <-- Deleted first element using del keyword")

##### Using pop method to remove and return last element in a list ########
a = my_list.pop()
print("Removed value: ", a)
print(my_list, " <-- Remaining list")
b = my_list.pop(2) # removes and returns the value at index 2
print("Removed from index 2: ", b)
print(my_list, " <-- Remaining list")

##### Slicing a list ########
left_my_list = my_list[:4]
right_my_list = my_list[4:]
print(left_my_list, " <-- Left slice")
print(right_my_list, " <-- Right slice")

##### Reversing a list by slicing ########
rev_my_list_slice = my_list[::-1]
print(rev_my_list_slice, " <-- List reversed by slicing")

##### List Comprehension ########
int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sqr_list = [n**2 for n in int_list]
print(int_list, " <-- List of integers")
print(sqr_list, " <-- List of squares of integers through list comprehension")

############################################
########### Other List methods #############
############################################
'''
my_list.clear() - removes all elements from list
my_list.index(element) - return index of first occurence of element in list
my_list.count(element) - return the count of number of occurences of element in list
my_list.sort(reverse = True) - returns list sorted in ascending order by default if no arguement is passed
'''

############################################
#### Other Built-in functions for list #####
############################################
'''
sum(my_list) - returns sum of all numbers in the list
reduce(function, my_list) - applies the function to all element in the list and returns value *** from functools import reduce ***
cmp(list1, list2) - return 1 if first list is greater than second list
max(my_list) - returns max value of a list
max(my_list) - returns min value of a list
all(my_list) - return True if all elements evaluate to True
enumerate(my_list) - returns index for the list elements
map(function, iterands of my_list) - returns a list after applying the function to each item of a given iterable
'''