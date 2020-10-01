#!/usr/bin/env python3

# import mmodules

import time

#x=2;y=3.4;z=1+2j    # if we want to declare variables in single line or multiple python statements separated by ; in one line
#print(x,y,z)        # print different variables in single line

print(f"Let's define few variables and check their data types or classes")
time.sleep(2)
x=10
y=4.5
z=1+2j
name="Inderpal Singh"
#name="x"           # even a single character enclosed inside "" is a string
bool_val_1=True
bool_val_2=False

print(f"The variables and their respective data types are as below,")
time.sleep(2)
print(x,type(x))
print(y,type(y))
print(z,type(z))
print(name,type(name))
print(bool_val_1,type(bool_val_1))
print(bool_val_2,type(bool_val_2))

