#!/usr/bin/env python3

# This script wil accept a path from user and identify if it's a file or a directory.
# The script will first check if the given path exists or not, if it exists then only script will proceed to check further if a file or not.

import os
import sys

os.system("clear")
user_path=input("Enter the path : ")

if os.path.exists(user_path):
    if os.path.isdir(user_path):
        print(f"{user_path} is a directory.")
    elif os.path.isfile(user_path):
        print(f"{user_path} is a file.")
    else:
        print(f"{user_path} couldn't be identified if a file or a directory.")
else:
    print(f"{user_path} doesn't exist on the system. Exiting script!")
    sys.exit(1)
