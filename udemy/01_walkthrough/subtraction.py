#!/usr/bin/env python3

# This script will perform subtraction of 2 numbers provided by user

import os
os.system("clear")	# clear screen
print(f"This script will perform subtraction of 2 numbers provided by user.\n")	# display purpose of script
print(f"The order of subtraction will be 'number1 - number2'\n")
a=eval(input("Enter first number : "))		# input number 1
b=eval(input("Enter second number : "))		# input number 2
difference=a-b					# performing subtraction
print(f"The difference of {a} and {b} is : {difference}\n")		# printing result
print(f"Giving back the prompt\n")
