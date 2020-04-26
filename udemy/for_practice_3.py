#!/usr/bin/env python3

# This script will accept a string from user and display its individual characters along with index values.
# Logic 2

import os
import platform

OS=platform.system()
if OS=="Linux":
    os.system("clear")
elif OS=="Windows":
    os.system("cls")

user_string=input("Enter string : ")
print(f"The string is : {user_string}")
print(f"length of string is : {len(user_string)}")
print(f"\nBelow is output of string in format: \n[character] --> [index_vaue]")
index_value=0
for i in user_string:
    print(f"{i} --> {index_value}")
    index_value+=1
