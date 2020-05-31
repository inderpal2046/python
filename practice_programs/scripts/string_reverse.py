###############################################################################
# File          : string_reverse.py
# Author        : Inderpal Singh Saini <inderpal2406@gmail.com>
# Created       : 31 May, 2020
# Updated       : 31 May, 2020
# Description   : A platform independent script to reverse a user entered string. 
################################################################################

# Import modules
import os
import platform
import sys
import re

# Define functions

def clearscreen():
    OS=platform.system()
    if OS=="Linux":
        os.system("clear")
    else:
        os.system("cls")
    return None

def string_reverse():
    mystring=input("Please enter a string : ")
    mylist=list(mystring)
    mylist.reverse()
    print(f"The reversed string is : {''.join(mylist)}")
    ans=input("\nDo you want to reverse another string? ")
    pattern1="[yY][eE][sS]"
    pattern2="[yY]"
    pattern3="[nN][oO]"
    pattern4="[nN]"
    if re.fullmatch(pattern1,ans) or re.fullmatch(pattern2,ans):
        string_reverse()
    elif re.fullmatch(pattern3,ans) or re.fullmatch(pattern4,ans):
        return None
    else:
        print(f"Invalid input. Please enter [yes|no] or [y|n]. The input can be case-insensitive. Exiting script!")
        sys.exit(1)
    return None

def main():
    clearscreen()
    print(f"This script will reverse the entered string.")
    string_reverse()
    print(f"End of Script :)")
    return None

if __name__=="__main__":
    main()
