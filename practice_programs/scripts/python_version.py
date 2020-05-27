###############################################################################
# File          : python_version.py
# Author        : Inderpal Singh Saini <inderpal2406@gmail.com>
# Created       : 28 May, 2020
# Updated       : 28 May, 2020
# Description   : Platform independent script to display python version. 
################################################################################

# import modules
import os
import sys
import platform

# Define functions

def clear_screen():
    OS=platform.system()
    if OS=="Linux":
        os.system("clear")
    else:
        os.system("cls")
    return None

def main():
    clear_screen()
    print(f"The python version is : {sys.version.splitlines()[0].split()[0]}")
    return None

if __name__=="__main__":
    main()
