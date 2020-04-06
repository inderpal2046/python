#!/usr/bin/env python3

# This script will convert text to lowercase based on user's choice.

import os
os.system("clear")

input_text=input("Enter the text : ")
print(input_text)
user_choice=input("Do you want to convert above text to lowercase? yes|no : ")

if user_choice=="yes":
    print(f"Output : {input_text.lower()}")
else:
    print(f"Cool if you don't want to convert text to lower case :)")
