#!/usr/bin/env python3

# Script to work with os.walk()

import os

#path="/home/inderpal2406/github/python"

#print(os.walk(path))      # simply writing os.walk(path) doesn't print any output, but with print statement, it prints a generator object
#list(os.walk(path))	   # prints no output
#print(list(os.walk(path))) # prints a list of tuples, in each tuple we have 3 values (one string and 2 lists - 1 of dir names & 2 of files
#for i in list(os.walk(path)): # using for loop, we have separated each tuple value in the complete list
#    print(i)

# python can understand generator object and can give same output as we get using for loop, 
# we use list to print for better understanding
#for i in os.walk(path):
#    print(i)

'''
# unpacking 3 values in each tuple
for dir_path,dir_list,file_list in os.walk(path):
    print(dir_path)	  # print all possibilities of dir_paths

print(f"----------------------------")

# unpacking 3 values in each tuple
for dir_path,dir_list,file_list in os.walk(path):
    print(dir_path,file_list)	# print all files in a particular dir_path

print(f"----------------------------")
for dir_path,dir_list,file_list in os.walk(path):
    print(dir_path,dir_list)	# print dir list or all dirs in the dir_path
'''

'''
for dir_path,dir_list,file_list in os.walk(path,topdown=False):	# by default topdown=True, making it False will reverse the order of printing
    print(dir_path,file_list)
'''

'''
os.system("clear")
path=input("Enter the directory path where we want to search the file : ")
req_file=input("Enter the filename which needs to be searched : ")
for dir_path,dir_list,file_list in os.walk(path):
    if len(file_list)!=0:		# we check only if files are present in the current dir_path
        if req_file in file_list:
            print(f"File {req_file} found in {dir_path}")
'''

# code to print all files in all sub-directories of a particular directory
os.system("clear")
path=input("Enter the directory path under which we want to list all files : ")
for dir_path,dir_list,file_list in os.walk(path):
    if len(file_list)!=0:
        print(f"\nFiles in {dir_path} are as below:")
        for i in file_list:
#            print(i)
             print(os.path.join(dir_path,i))	# to print complete path of file
