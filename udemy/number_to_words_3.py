#!/usr/bin/env python3

# This script presents third alternative way to convert an entered number in 1 to 10 range to words.

import os
os.system("clear")

number=eval(input("Enter a whole number between 1 to 10 : "))

num_dict={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten"}

if number in [1,2,3,4,5,6,7,8,9,10]:
    print(f"{num_dict.get(number)}")
else:
    print(f"You entered an invalid number {number}. Please enter a whole number between 1 to 10 range.")
