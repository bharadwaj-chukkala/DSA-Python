'''
This file contains the functions that are used to manipulate the string
'''

'''
* String Data Sctructure represents sequence of characters
* Immutable
'''

##### Creating a string ########
my_str = 'Hello'
my_str2 = "World"
my_str3 = '''Happy to see y'all'''
print(my_str + " " + my_str2 + ". " + my_str3 + "!")

##### Accessing elements of a string ########
my_str = "There is a need for speed"
print(my_str, " <-- My initial string is")
print(my_str[0], " <-- The first element of our string is")

##### Slicing a string ########
print(my_str[:5], " <-- The first five elements sliced")

##### Reversing a string ########
# 1. By slicing
print(my_str[::-1], " <-- My string reversed by slicing")

# 2. By using builtin join and resversed functions
print("".join(reversed(my_str)), " <-- My string reversed by in built functions")

##### Updating elements of a string ########
'''Since strings are immutable there's only one way to do it
convert string to a list, update elements and join them back into a string
'''
my_str = "Converdation"
print(my_str, " <-- Incorrect spelling")
my_str_lst = list(my_str)
my_str_lst[6] = 's'
my_str_new = "".join(my_str_lst)
print(my_str_new, " <-- Updated string with correct spelling")

##### Deleting elements of a string ########
'''
Since strings are immutable, we cannot delete individual elements
we can delete elements by slicing and forming a whole new string
'''
print(my_str_new, " <-- Printing the current string")
my_str_changed = my_str_new[:7] + my_str_new[9:]
print(my_str_changed, "<-- String with deleted elements")

# del my_str_changed # deletes entire string

##### Length of a string ########
print(len(my_str_new), " <-- Length of the string")

##### Modifying a string ########
# 1. Convert all elements to uppercase
upper_str = my_str_new.upper()
print(upper_str, " <-- String in all caps")

# 2. Convert all elements to lowercase
lower_str = my_str_new.lower()
print(lower_str, " <-- String with no caps")

# 3. Remove leading and trailing whitespace
my_str = "     There is a need for speed         "
no_wspace = my_str.strip()
print(my_str, " <-- Initial String")
print(no_wspace, " <-- String with no whitespace")

# 4. Replace string -- modifies element and creates a new string
my_str = "Converdation"
print(my_str, " <-- Incorrect spelling")
my_str_new = my_str.replace('d', 's')
print(my_str_new, " <-- Updated string with correct spelling using the replace method")

# 5. Split string -- at a key seperator point -- returns a list with substrings separated by the separator
my_str = "Hello, World"
sub_Str_list = my_str.split(',')
print(sub_Str_list, " <-- list of separated substrings")


##### Format string ########
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

print("{} {} {}".format('Bros', 'For', 'Life'))
print("{2} {0} {1}".format('Bros', 'For', 'Life'))

############################################
########### Other String methods #############
############################################
'''
my_str.capitalize() - returns new string with First char in uppercase
my_str.find(element) - return index of first char or first occurence of element in string
my_str.count(element) - return the count of number of occurences of element in string
my_str.isalnum() - return True if all elements are alphanumeric
my_str.isalpha() - returns True if all elements are alphabetic
'''