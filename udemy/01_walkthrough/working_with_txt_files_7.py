#!/usr/bin/env python3

# read all data and stroe it as a list and then print line by line

fo=open("friends.txt","r")
data=fo.readlines()
fo.close()
for i in range(3):
    print(f"{data[i]}")

# to print line by line all lines
fo=open("friends.txt","r")
data=fo.readlines()
fo.close()
for i in list(range(len(data))):
    print(f"{data[i]}")

# print the first line only
print(f"{data[0]}")

# print last line only
print(f"{data[-1]}")
