#!/usr/bin/env python3

# this script will calculate x raised to y answer

import os
os.system("clear")
print(f"This script will calculate x raised to y answer.\n")
x=eval(input("Enter value of x : "))
y=eval(input("Enter value of y : "))
ans=x**y
print(f"\nThe answer of {x} raised to {y} is : {ans}\n")
