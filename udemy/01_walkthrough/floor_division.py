#!/usr/bin/env python3

# This script will perform floor division of 2 numbers provided by user

import os
os.system("clear")
print(f"This script will perform floor division of 2 numbers provided by user.\n")
print(f"The division will be in format as 'dividend/divisor'.\n")
dividend=eval(input("Enter dividend : "))
divisor=eval(input("Enter divisor : "))
quotient1=dividend/divisor
quotient2=dividend//divisor
print(f"\nThe quotient of simple division is : {quotient1}\n")
print(f"Since the quotient in floor division is round off to nearest lower number, its value is : {quotient2}\n")
