#!/usr/bin/env python3

# This script will ask for user input and perform an action on the user input string
# Action can be conversion of user input string to lower, upper, title or swap case

import os
os.system("clear")

user_string=input("Enter the string : ")
user_action=input("Enter the action (Note action can take values such as [lower|upper|title|swapcase] : ")

if user_action=="lower":
    print(f"{user_string.lower()}")
elif user_action=="upper":
    print(f"{user_string.upper()}")
elif user_action=="title":
    print(f"{user_string.title()}")
elif user_action=="swapcase":
    print(f"{user_string.swapcase()}")
else:
    print(f"You hhave entered an invalid choice. Please enter action values as [lower|upper|title|swapcase] only.")
