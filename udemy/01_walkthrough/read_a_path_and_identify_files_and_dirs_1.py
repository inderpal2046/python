#!/usr/bin/env python3

# This script will read user input.
# User will provide a directory path and the script will test if it exists or not.
# If it exists, then list the files and directories in it.
# This functionality can be achieved using 2 types of logic.
# Here is type 1 of logic. 

import os
import sys

os.system("clear")

path=input("Enter the directory path : ")

if os.path.exists(path):
    if os.path.isdir(path):
        for dir_path,dir_list,file_list in os.walk(path):
            print(f"Directory path is : {path} \n")
            print(f"Directories found in {path} are as follows:")
            for i in dir_list:
                print(i)
            print(f"\nFiles found in {path} are as follows:")
            for i in file_list:
                print(i)
            break
    else:
        print(f"Entered path is not a directory. Please enter a directory path. Exiting script!")
        sys.exit(1)
else:
    print(f"{path} doesn't exist on system. Exiting script!")
    sys.exit(2)
