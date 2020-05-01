# This script works on both Linux as well as Windows. So, we have not included shebang here.
# This script will accept a directory path in which files older than x days will be removed. This age of x days can be set using age variable.
# This script will not remove files having age more than x days for now, but will only display their names.


# Import modules
import os
import platform
import sys
import datetime


# Setting up age of files in days, this means files older than x days will be removed.
age=30


# Code to clear screen irrespective of OS type
OS=platform.system()
if OS=="Linux":
    os.system("clear")
else:
    os.system("cls")


# Code to take user input of path and test if it exists and is not a file. We need directory path only which exists.
path=input("Enter the directory path [/tmp|/var/log|C:\\Users\\|D:\\Programs|etc] : ")
if not os.path.exists(path):
    print(f"Entered path does not exist. Please enter a valid directory path.")
    sys.exit(1)
elif os.path.isfile(path):
    print(f"Entered path is a file. Please enter a directory path.")
    sys.exit(2)


# Code to check age of each file in given directory and remove them if found to be older than x days.
count=0					# initiate count=0 so that if no file is found to be older than x days, then display simple output
for i in os.listdir(path):
    j=os.path.join(path,i)		# join operation to get complete path of files, we need complete paths
    if os.path.isdir(j):		# if current j is a dir then skip it as we won't go inside sub-directories to check
        continue
    last_atime_secs=os.path.getatime(j)	# get the last access time in seconds, i guess these seconds are calculated since system start
    last_atime=datetime.datetime.fromtimestamp(last_atime_secs) # convert last atime in secs to a date and time stamp
    current_time=datetime.datetime.now()	# store current date and time into a variable
#   difference_in_time=current_time-last_atime	# calculate differnce in last access time and current date and time
#   print(f"{dir(current_time-last_atime)}")
    difference_in_days=(current_time-last_atime).days # see important note in the end
    if difference_in_days>30:
        print(f"The file {j} is {difference_in_days} days old.")
        count+=1			# increment count as we found file older than x days
if count==0:				# to check if count was not incremented after testing all files in the directory
    print(f"No files found to be older than 30 days.")


# Important note
# difference_in_days=(current_time-last_atime).days 
# Above statement will calculate differnce between last access time and current time in terms of days 
# This is an example of operation on an object. Differnce between 2 objects and operation on top of that.
# To check list of operations available on top of operation on 2 objects, dir(current_time-last_atime)
