###############################################################################
# File          : time.py
# Author        : Inderpal Singh Saini <inderpal2406@gmail.com>
# Created       : 30 May, 2020
# Updated       : 30 May, 2020
# Description   : A platform independent script to display time of current timezone.
#		: Time of other timezones can also be dispayed as per user input.
################################################################################

# Defining colors
RED="\033[0;31m"
OR="\033[0;33m"
NC="\033[0m"

# Import modules
import os
import platform
import sys
from datetime import datetime
# try and except block to catch ModuleNotFoundError error while importing pytz module which is a non-default module
try:
    import pytz
except ModuleNotFoundError:
    print(f"{RED}Module 'pytz' not found{NC}")
    print(f"Please install this non-default module first and then execute this script. Exiting script!")
    sys.exit()

# Define functions

def clearscreen():
    OS=platform.system()
    if OS=="Linux":
        os.system("clear")
    else:
        os.system("cls")
    return None

def time(place):
    if place=="current":
        print(f"Time at current geographical place is as below:")
        print(datetime.now().strftime("%d-%m-%Y  %H:%M:%S"))
    elif place=="other":
        print(f"{OR}NOTE: Python provides 590 different timezone options.")
        print(f"Owing to space constraints, we list every 40th item from the 590 timezone options.")
        print(f"Please select the nearest timezone to your desired timezone from below options:{NC}")
        tz_list=pytz.all_timezones[0::40]
        for i in tz_list:
            index_value=tz_list.index(i)
            print(f"{index_value+1}.{i}")
        #try except block to catch ValueError exception of undesired input by user
        try:
            tz_number=int(input("Time in which timezone from above options do you want to check? [1|2|3|..|14|15] : "))
        except ValueError:
            print(f"{RED}Invalid input.{NC} Please enter a number [1|2|3|..|14|15] as input. Exiting script!")
            sys.exit(1)
        index_value=tz_number-1
        tz=tz_list[index_value]
        print(f"Time at {tz} timezone is as below:")
        tz_object=pytz.timezone(tz)
        print(datetime.now(tz_object).strftime("%d-%m-%Y  %H:%M:%S"))
    else:
        print(f"{RED}Invalid input{NC}. Please enter [current|other] options only. Exiting script!")
        sys.exit(1)
    return None

def main():
    clearscreen()
    print(f"Welcome :)")
    zone=input("Which timezone's time do you want to check? [current|other] : ")
    time(zone)
    return None

if __name__=="__main__":
    main()
