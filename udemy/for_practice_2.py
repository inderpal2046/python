#!/usr/bin/env python3

# This script will accept a string from user and display its individual characters along with index values.
# Logic 1

import os
os.system("clear")

user_string=input("Enter the string : ")
print(f"The string entered is : {user_string}")
print(f"Length of string is : {len(user_string)}")
print(f"Below is the output of script in format,\n[string_character] --> [character_index]")
for i in range(0,len(user_string)):
    print(f"{user_string[i]} --> {i}")
