# This script will ask for user to provide extension of file and location where the file needs to be searched
# Since this script can be run on Linux and Windows we won't use shebang at the start


# Importing different modules of python
import os
import platform
import sys


# Code to clear screen irrespective of the OS
OS=platform.system()
if OS=="Windows":
    os.system("cls")
elif OS=="Linux":
    os.system("clear")


# Ask user input for directory to be searched
path_to_search=input("Enter the directory where we need to search [/tmp|/etc|/var/log|/root|etc]: ")


# Code to check if provided dirctory is a directory or not. If not then exit with specific message
if os.path.isdir(path_to_search):		# if provided directory is a directory then check if it is empty or not
    list_of_contents=os.listdir(path_to_search)
    no_of_contents=len(list_of_contents)
    if no_of_contents==0:			# if directory is empty then exit with specific message
        print(f"The directory {path_to_search} is empty.")
    else:					# if directory is not empty then ask for file extension to be searched
        required_extension=input("Enter extension of file that needs to be searched [.sh|.py|.log|.txt|etc]: ") 
        print(f"The files in {path_to_search} ending with {required_extension} are as follows:")
        count=0
        for i in list_of_contents:
            if i.endswith(required_extension):	# as path is treated as a string, we use string operation to check end of each element 
                print(i)
                count+=1
        if count==0:
            print(f"Sorry! We searched but there are no files ending with {required_extension} in {path_to_search}")
        else:
            print(f"We found total {count} files with extension {required_extension} in {path_to_search}")
else:
    print(f"The given path \"{path_to_search}\" is not a directory. Please enter a valid path of a directory to search in.")
    print(f"Exiting script.")
    sys.exit(1)


# The output of searched files can be stored in a list instead of printing the output one by one
# For this, we need to define an empty list and go on appending elements to it as we find a match for required extension
# Then the logic to check if any files with required extension were found or not will also change. Length of list can be used.
# As of now this script will work if valid directory names are provided. 
# If we provide an invalid directory path, then also this script will work because of the logic used.
# but going forward we'll learn how to catch the error of invalid directory names.
