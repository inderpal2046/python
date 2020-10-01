#!/usr/bin/env python3

# This script will accept user input as a numbr from 1 to 10 and display it in words.

import os
os.system("clear")

number=eval(input("Enter a number between 1 to 10 : "))
if number==1:
    print(f"You entered one.")
elif number==2:
    print(f"You entered two.")
elif number==3:
    print(f"You entered three.")
elif number==4:
    print(f"You entered four.")
elif number==5:
    print(f"You entered five.")
elif number==6:
    print(f"You entered six.")
elif number==7:
    print(f"You entered seven.")
elif number==8:
    print(f"You entered eight.")
elif number==9:
    print(f"You entered nine.")
elif number==10:
    print(f"You entered ten.")
else:
    print(f"You entered an invalid number {number}. Only whole numbers between 1-10 are accepted.")
