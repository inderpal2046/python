#!/usr/bin/env python3

fo=open("friends.txt","r")
print(fo.read())
fo.close()

# OR

fo=open("friends.txt","r")
data=fo.read()
fo.close()
print(data)

# reading line by line

fo=open("friends.txt","r")
print(fo.readline())	# This will read only first line and print, to read and print next lines, we need to have subsequent readline()
print(fo.readline())
fo.close()
