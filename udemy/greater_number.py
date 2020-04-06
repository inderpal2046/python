#!/usr/bin/env python3

# This script will accept 2 numbers as input, compare them and print the greater number.

import os
os.system("clear")

number_1=eval(input("Enter first number : "))
number_2=eval(input("Enter second number : "))

if number_1>number_2:
    print(f"{number_1} is greater.")
elif number_2>number_1:
    print(f"{number_2} is greater.")
else:
    print(f"Both numbers are equal.")
