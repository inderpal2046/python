#!/usr/bin/env python3

###############################################################################
# File          : numbers_to_list_and_tuple.py
# Author        : Inderpal Singh Saini <inderpal2406@gmail.com>
# Created       : 07 Nov, 2020
# Updated       : 07 Nov, 2020
# Description   : A script to accept user input in form of comma separated numbers.
#		: Then it'll genarate a list and a tuple from those numbers.
#		: Enhancement needs to be added which is the ability to detect wrong input.
################################################################################

# Import modules

import os
import platform
import sys

# Detect the OS and clear the screen.

if platform.system()=="Windows":
  os.system("cls")
elif platform.system()=="Linux":
  os.system("clear")
else:
  print(f"The operating system couldn't be identified. Exiting script!")
  sys.exit(1)

# Print the purpose of the script.

print(f"The script accepts input as comma separated numbers and generate a list and tuple from those numbers.")

# Accept user input.

print(f"Please provide input in the form of: 1,2,3,4")
user_str=input("Enter the comma separated numbers: ")

# Split the user input string with comma as a delimiter. 
# This split operation automatically results into a list as an output.

numlist=user_str.split(",")

# Convert the list to tuple and store it in a separate variable.

numtup=tuple(numlist)

# Print output

print(f"The list is: {numlist}")
print(f"The tuple is: {numtup}")
