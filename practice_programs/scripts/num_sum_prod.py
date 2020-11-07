#!/usr/bin/env python3

###############################################################################
# File          : num_sum_prod.py
# Author        : Inderpal Singh Saini <inderpal2406@gmail.com>
# Created       : 07 Nov, 2020
# Updated       : 07 Nov, 2020
# Description   : A script to present food to animals.
#		: This script demonstrates calling of another script from within a script.
#		: The food.sh script is called with arguments passed to zoo.sh
#		: Depending on the exit status of food.sh, further processing is performed.
################################################################################

# Import modules.

import os
import platform
import sys

# Detect OS and clear screen.

if platform.system()=="Windows":
  os.system("cls")
elif platform.system()=="Linux":
  os.system("clear")
else:
  print("The operating system couldn't be identified. Exiting script!")
  sys.exit(1)

# Display purpose of script.

print(f"This script will accept a number 'n' and number of iterations.")
print(f"Then it will display the output of n+nn+nnn+... as per the number of iterations.")

# Accept user input.

num=int(input("Please enter the number: "))
iterations=int(input("Please enter the number of iterations: "))

# For loop to iterate over number of iterations and calculate the sum.

for i