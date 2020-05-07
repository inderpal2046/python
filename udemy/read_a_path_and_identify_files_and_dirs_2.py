#!/usr/bin/env python3

# This script will read user input.
# User will provide a directory path and the script will test if it exists or not.
# If it exists, then list the files and directories in it.
# This functionality can be achieved using 2 types of logic.
# Here is type 2 of logic. 

import os
import sys

os.system("clear")
path=input("Enter the path : ")

if os.path.exists(path):
    if os.path.isdir(path):
        for i in os.listdir(path):
            full_path=os.path.join(path,i)
            if os.path.isdir(full_path):
                print(f"{full_path} is a directory.")
            elif os.path.isfile(full_path):
                print(f"{full_path} is a file.")
            else:
                print(f"File type of {os.path.join(path,i)} couldn't be identified as a file or a directory.")
    else:
        print(f"{path} is not a directory. Please enter a directory path. Exiting script!")
        sys.exit(1)
else:
    print(f"{path} doesn't exist on the system. Please enter a valid directory path. Exiting script!")
    sys.exit(2)
