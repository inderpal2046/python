#!/usr/bin/env python3

# A script to change directory and handle excepts if occurred while changing directory
# complete script is written in terms of functions

import os

def clearscreen():
    os.system("clear")
    return None

def main():
    clearscreen()
    req_path=input("Enter the directory path to change to : ")
    print(f"Current working directory is : {os.getcwd()}")
    try:
        os.chdir(req_path)
        print(f"New working directory is : {os.getcwd()}")
    except FileNotFoundError:
        print(f"{req_path} is not present on the system. Please enter a valid path.")
    except NotADirectoryError:
        print(f"{req_path} is not a directory but a file. Sorry we can't change directory.")
    except PermissionError:
        print(f"Sorry we don't have required privileges to change directory to {req_path}")
    except Exception as error:
        print(error)
    return None

if __name__=="__main__":
    main()
