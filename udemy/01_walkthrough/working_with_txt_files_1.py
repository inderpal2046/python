#!/usr/bin/env python3

# In this script we'll learn to create an empty file, print the mode in which it has been opened, check the mode.

'''
# code to just create an empty txt file named newfile.txt
fo=open("name.txt","w")
fo.close()
'''

# code to print modein which file has been opened and check the mode
fo=open("newfile.txt","w")
print(f"{fo.mode}")		# prints mode of file in which it is open
print(f"{fo.readable()}")	# gives boolean output based on condition if our file is opened in readable mode or not
print(f"{fo.writable()}")
fo.close()

