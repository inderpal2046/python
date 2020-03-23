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

name="Inder"
print(name)
print(name[0])
print(name[1])
print(name[4])
