#!/usr/bin/env python3

# Defining string using three different ways in python3

'''
my_name='Inderpal Singh Saini'
my_company="Capgemini Technology Services India Ltd."
my_info="""I live in Mumbai and I work as a DevOps professional."""
print(f"My name is {my_name}. \nMy company name is {my_company} \n{my_info}")
'''

'''
my_name='Inderpal Singh Saini'
my_company="Capgemini Technology Services India Ltd."
my_info="""I live in Mumbai.
I work as a DevOps professional.
I like reading books."""
print(f"My name is {my_name}. \nMy company name is {my_company} \n{my_info}")
'''

# To test is a string is null or not

'''
string_1=""
string_2=" "
print(f"First string is not null: {bool(string_1)}")
print(f"Second string is not null: {bool(string_2)}")
'''

# To print a string variable in different ways

'''
string_1="Python Scripting"
print(f"{string_1}")
print(string_1)
'''

# To check if same string stored in 2 different variables will have same memory location or different

'''
string_1="Python Scripting"
string_2="Python Scripting"
string_3="python Scripting"
print(f"memory location of string_1 variable is: {id(string_1)}")
print(f"memory location of string_2 variable is: {id(string_2)}")
print(f"memory location of string_3 variable is: {id(string_3)}")
'''

# To print specific characters of the string 

'''
name="Inder"
print("Below are positive index values serially,")
print(name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print()
print("Below are negative index values serially,")
print(name)
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
'''

# Print a range of characters.

'''
name="Inderpal"
print(name)
print(name[0:5])	# Start print from 0 index and print 5 characters
print(name[0:])		# Start print from 0 index and print till last character
nickname=name[0:5]	# save output string
print(nickname)		# print output string
print(name[:5])		# start from index 0 and go upto one index less than the mentioned index 5
print(name[2:5])	# start from index 2 and go upto one index less than the mentioned index 5
'''

# Modifying string characters

'''
name="Inderpal"
#name[0]="U"		# error, string object does not support item assignment
#del name[3]		# error
print(name)
del name		# success
print(name)		# error
'''

# Length of string

'''
name="Inderpal Singh Saini"
length=len(name)
print(f"Length of the string is: {length}")
print(f"Length of the string is: {len(name)}")
'''

# Add or concatenate 2 strings

string_1="Python"
string_2="Scripting"
string_3=string_1+string_2
print(string_3)
string_4=" "
string_5=string_1+string_4+string_2
print(string_5)
string_6=string_1+" "+string_2
print(string_6)
string_7=string_1+" "+string_2+" "+"tutorials"
print(string_7)
