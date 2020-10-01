#!/usr/bin/env python3

# This script will accept a string.
# Then check if input string is in title format or not
# If not then convert it to title format and print

import os
os.system("clear")

input_string=input("Enter the string: ")
if input_string.istitle():
    print(f"Your string is already in title format.")
else:
    print(f"The input string in title format is as below: \n{input_string.title()}")
