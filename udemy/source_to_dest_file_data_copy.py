# Script to copy data from source txt file to destination txt file. 
# Not necessary that the files must be txt files. It can be any file with any extension, but must be a file.


# Defining source and destination txt files with complete paths
#sfile="/home/inderpal2406/tmp/source.txt"
#dfile="/home/inderpal2406/tmp/dest.txt"


# We want the user to input source and destination file path and name.
# So, modifying code as per above requirement


# Importing modules
import os
import sys
import platform


# Clearing screen irrespetive of OS
OS=platform.system()
if OS=="Linux":
    os.system("clear")
else:
    os.system("cls")


# Getting user input for source file
sfile=input("Enter source txt file path and name [/tmp/data.txt|C:\\Users\\tmp.txt] : ")


# Test if sfile exists or not, if exists then is it a dir or a txt file. Then further process it.
if os.path.exists(sfile):
    if os.path.isdir(sfile):
        print(f"Mentioned path is a directory. Please enter path of a txt file. \nExiting script.")
        sys.exit(1)
    elif os.path.isfile(sfile):
        print(f"File exists")
        dfile=input("Enter destination txt file path and name [/opt/data.txt|C:\\Tmp\\tmp.txt] : ")
        sfo=open(sfile,"r")	# if we just mention sfo=open(sfile), then by default file gets opened in read mode
        data=sfo.read()		# store entire data as string, readline() as string but line by line, and readlines() as list for entire data
        sfo.close()
        dfo=open(dfile,"w")
        dfo.write(data)
        dfo.close()
        print(f"{sfile} copied into {dfile}")
    else:
        print(f"Unknown file type. Please enter path of a txt file. \nExiting script.")
        sys.exit(1)
else:
    print(f"Mentioned path/file does not exists. \nExiting script.")
    sys.exit(1)
