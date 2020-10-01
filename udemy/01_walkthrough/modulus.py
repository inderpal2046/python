#!/usr/bin/env python3

# This script will calculate remainder of division of 2 numbers

import os
os.system("clear")
print(f"This script will calculate remainder of division of 2 numbers.\n")
print(f"The division will be in the form of 'dividend/divisor' \n")
dividend=eval(input("Enter dividend : "))
divisor=eval(input("Enter divisor : "))
remainder=dividend%divisor
print(f"\nThe remainder of {dividend}/{divisor} is : {remainder}\n")
