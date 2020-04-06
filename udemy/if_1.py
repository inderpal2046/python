#!/usr/bin/env python3

# This script is to practise if construct
# We'll allign text based on user's input

import os
os.system("clear")

input_string=input("Enter the text : ")
print(input_string)
user_choice=input("Do you want the text to be alligned while printing? yes|no : ")

if user_choice=="yes":
    width=os.get_terminal_size().columns
    print(f"{input_string.ljust(width)}")
    print(f"{input_string.rjust(width)}")
    print(f"{input_string.center(width)}")
