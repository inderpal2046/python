#!/usr/bin/env python3

# This script will accept 2 numbers as user input and divide them.
# If user enters divisor as zero, then divide by zero exception is handled.

import os
os.system("clear")

dividend=eval(input("Enter the dividend : "))
divisor=eval(input("Enter the divisor : "))

try:
    quotient=dividend/divisor
    print(f"Quotient = {quotient}")
except:
    print(f"Division by zero results into infinity. Please enter a non-zero divisor.")
