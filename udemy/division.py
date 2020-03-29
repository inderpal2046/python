#!/usr/bin/env python3

# This script will perform division of 2 numbers provided by user

import os
os.system("clear")
print(f"This script will perform division of 2 numbers provided by user.\n")
print(f"The operation will be like : dividend/divisor \n")
dividend=eval(input("Enter the dividend : "))
divisor=eval(input("Enter the divisor : "))
quotient=dividend/divisor
print(f"The quotient of {dividend}/{divisor} is : {quotient} \n")
