#!/usr/bin/env python3

# A pre-defined list of numbers is present.
# User enters an index value and script will fetch that index value from list.
# Script handles exception of index value out of range if user enters an out of range index value.

import os
os.system("clear")

my_list=[1,2,3,4,5,6,7,8]
print(f"We have a pre-defined list of numbers.")
index=eval(input("Which index value do you want to fetch? [0|2|5|etc] : "))

try:
    print(f"The value at index {index} in the list is : {my_list[index]}")
except Exception as error:
    print(error)
