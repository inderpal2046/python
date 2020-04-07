#!/usr/bin/env python3

# This script presents an alternative logic to print a number within 1 to 10 range into words.

import os
os.system("clear")

number=eval(input("Enter a whole number from 1 to 10 : "))

if number in [1,2,3,4,5,6,7,8,9,10]:
    if number==1:
        print(f"One")
    elif number==2:
        print(f"Two")
    elif number==3:
        print(f"Three")
    elif number==4:
        print(f"Four")
    elif number==5:
        print(f"Five")
    elif number==6:
        print(f"Six")
    elif number==7:
        print(f"Seven")
    elif number==8:
        print(f"Eight")
    elif number==9:
        print(f"Nine")
    else:
        print(f"Ten")
else:
    print(f"You entered an invalid number {number}. Please enter a whole number between range 1-10.")
