#!/usr/bin/env python3

# Script to demonstrate exception handling of file not present.
# Script will accept a file path from user and display content of it.
# Script handles the exception of file not present.

import os
os.system("clear")

file=input("Enter the full path of file : ")

try:
    fo=open(file,"r")
    data=fo.read()
    print(data)
    fo.close()
except Exception as error:
    print(error)
