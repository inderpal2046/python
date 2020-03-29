#!/usr/bin/env python3

# This script will perform addition of 2 numbers received from user

# clearing screen

import os
os.system("clear")

# print purpose of sript

print("This script will perform addition of 2 numbers.")

# reading input from user

a=eval(input("Enter first number: "))
b=eval(input("Enter second number: "))

# calculating sum

sum=a+b

# displaying result

print(f"The sum of {a} and {b} is {sum}.")
