#!/usr/bin/env python3

fo=open("friends.txt","r")
print(fo.read())
fo.close()

# OR

fo=open("friends.txt","r")
data=fo.read()
fo.close()
print(data)
