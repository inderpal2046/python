#!/usr/bin/env python3

# This script will print a list, then each element in the list and also if that element is even or odd number.

import os
os.system("clear")

my_list=[1,2,45,6,3,88,7,6,99]
print(f"The list is : {my_list}\n")

for i in my_list:
    remainder=i%2
    if remainder==0:
        print(f"{i} is an even number.")
    else:
        print(f"{i} is an odd number.")
    os.system("sleep 1")

print(f"\nThis is the end of loop.")
