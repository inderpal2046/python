'''
In Linux, we need to switch to root user using su command inorder to execute this script so that this script is able to search all directories with super user privileges.
This script is platform independent.
'''


# Importing modules
import os
import string	# required to check which drives are present
import platform


# Code to check which OS
OS=platform.system()
if OS=="Linux":
    os.system("clear")
    path="/"
    req_file=input("Enter the file name to be searched : ")
    for dir_path,dir_list,file_list in os.walk(path):
        if len(file_list)!=0:
            if req_file in file_list:
                #print(f"File {req_file} found in {dir_path}")
                print(os.path.join(dir_path,req_file))
else:
    os.system("cls")
    req_file=input("Enter the file name to be searched : ")
    #code to check which drives are present
    drives_on_sys=[]	# an empty list to collect drive names for drive present on system
    for i in string.ascii_lowercase:
        if os.path.exists(i+":\\"):
            #print(f"{i}:\\")
            drives_on_sys.append(i+":\\")	# the list gets appended with drive names which are present on system
    #print(f"Drives present on system are : {drives_on_sys}")
    #code to search req_file in all drives on Windows OS 
    for each_drive in drives_on_sys:
        #for dir_path,dir_list,file_list in os.walk("C:\\"):
        for dir_path,dir_list,file_list in os.walk(each_drive):
            if len(file_list)!=0:
                if req_file in file_list:
                    print(os.path.join(dir_path,req_file))


'''
# Alternate logic for searching file, can be used in Linux as well as Windows
os.system("clear")
path="/"
req_file=input("Enter the file name to be searched : ")
for dir_path,dir_list,file_list in os.walk(path):
    if len(file_list)!=0:
        for i in file_list:
            if i==req_file:
                print(os.path.join(dir_path,i))
'''
