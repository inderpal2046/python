#!/usr/bin/env python3

###############################################################################
# File          : first_and_last.py
# Author        : Inderpal Singh Saini <inderpal2406@gmail.com>
# Created       : 07 Nov, 2020
# Updated       : 07 Nov, 2020
# Description   : A script to accept comma separated values from user.
#		: Then split it on basis of comma.
#		: This will automatically convert it to a list.
#		: Then display the first and last element.
################################################################################


# Import modules.

import os
import platform
import sys

# Detect the OS and clear screen.

if platform.system()=="Windows":
  os.system("cls")
elif platform.system()=="Linux":
  os.system("clear")
else:
  print(f"The OS couldn't be identified. Exiting script!")
  sys.exit(1)

# Display purpose of script.

print(f"The script will accept comma separated values from user and then display the first and last elements from the input.")

# Accept user input.

print(f"Please provide the input in form of: cat,bat,rat,mat,1,1.33")
user_str=input("Please enter the comma separated values: ")

# Split the input string with comma as delimiter.

userlist=user_str.split(",")

# Display the first and last element.

print(f"First element: {userlist[0]}")
print(f"Last element: {userlist[-1]}")