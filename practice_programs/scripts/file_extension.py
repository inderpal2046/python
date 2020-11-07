#!/usr/bin/env python3

###############################################################################
# File          : file_extension.py
# Author        : Inderpal Singh Saini <inderpal2406@gmail.com>
# Created       : 07 Nov, 2020
# Updated       : 07 Nov, 2020
# Description   : A script to accept a filename from the user and print the extension of that.
#		: The enhancement to enable the script to detect no file extension needs to be added.
#		: Maybe we can use str.rsplit(sep=".", maxsplit=1) function to add the enhancement.
################################################################################

# Import modules

import os
import platform
import sys

# Detect the OS and clear the screen accordingly.

if platform.system()=="Windows":
  os.system("cls")
elif platform.system()=="Linux":
  os.system("clear")
else:
  print(f"The operating system couldn't be detected. Exiting script!")

# Display purpose of script.

print(f"The script will accept a filename and print its extension.")

# Accept user input for filename with extension

filename=input("Please enter the filename, (for example: name.txt): ")

# Split the input filename based on dot/period as a delimiter .

tmplist=filename.split(".")

# The extension will be the last element of the list.

extension=tmplist[-1]

# Print the extension.

print(f"The extension of file is: {extension}")

# Single line implementation of above code is as below,

#print(f"The extension of file is: {filename.split('.')[-1]}")

