#!/usr/bin/env python3


# Infinite loop
'''
while True:
    print(f"Hello from while loop")
    print(f"---------------------")
'''


# Suppose we want to monitor our file system continuously after each second
'''
import time
while True:
    print(f"Logic to check file system utilization.")
    time.sleep(1)
'''


# suppose we don't want to execute our loop infinitely and need to stop it in between, then
my_number=1
while my_number<=10:
    print(my_number)
    my_number+=1 
# this is called as stopping the while loop based on a condition.
# loop will be executed while the condition is True
