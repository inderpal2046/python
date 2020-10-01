#!/usr/bin/env python3

# importing modules
import time

print(f"Let's define two variables x and y")
x=2
y=0.9
time.sleep(2)
print(f"x=2\ny=0.9")
time.sleep(2)
print(f"Value of variable x is {x} \nValue of variable y is {y}")
time.sleep(2)
print(f"Let's find out data type/class of vairables")
time.sleep(2)
print(f"Data type of variable x is {type(x)}\nData type of variable y is {type(y)}")
time.sleep(2)
print(f"Re-declaring the variable x or updating value of variable x")
time.sleep(2)
x=10
print(f"x=10")
time.sleep(2)
print(f"New value stored in variable x is {x} and data type of x is now {type(x)}")
time.sleep(2)
print(f"Let's delete the variable y as it is no lenger needed. This will free up RAM space and improve performance")
time.sleep(2)
del y
print(f"Variable y is deleted")
time.sleep(2)
print(f"Let's have a look at rules to define variable names")
time.sleep(2)
print(f"1. Variable name should contain letters, numbers and underscore.")
time.sleep(2)
print(f"2. Variable name should not contain special characters/symbols like !@#$% etc.")
time.sleep(2)
print(f"3. Variable name should not be same as a keyword in python, for example, if, then, print, try, etc.")
time.sleep(2)
print(f"4. Variable name should not contain space, instead use an underscore if needed to combine multiple words as same var name.")
time.sleep(2)
print(f"5. Variable name should not start with a number.")
time.sleep(2)
print(f"6. Variable names are case sensitive.")
time.sleep(2)
print(f"7. Variable name can start with an underscore.")
time.sleep(2)

