#!/usr/bin/env python3

# This script will accept user input as a string.
# Then display this string in left, right, center of a line in title format.

string=input("Enter the string: ")	# read input string
string=string.title()			# convert string to title format

'''
# in windows cmd, mode command tells us width of a line as 122, need to check similar command in linux
# in linux terminal, 'tput cols' and 'tput rows' commands lets us know the no of columns and rows in terminal, respectively
# its 142 cols in linux terminal
print(f"{string.ljust(142)}")		# display to left
print(f"{string.center(142)}")		# display at center
print(f"{string.rjust(142)}")		# display to right
'''

# this script may not display output properly if run on linux/windows terminal on other system.
# So, to overcome this, we'll use os module

import os
width=os.get_terminal_size().columns
print(f"{string.ljust(width)}")
print(f"{string.center(width)}")
print(f"{string.rjust(width)}")

# or instead of converting the string to title format separately,
# print(f"{string.ljust(width).title()}")
# we can apply title operation befor ljust operation
