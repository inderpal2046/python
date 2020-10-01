#!/usr/bin/env python3

# Script to demonstrate calling a function from a function

# defining function

def add(int1,int2):	# parameter
    sum=int1+int2
    return sum

def average():
    total=add(4,5)	# argument, also calling a function from another function
    average=total/2
    print(f"Average: {average} ")

average()
