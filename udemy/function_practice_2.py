#!/usr/bin/env python3

# Simple script to practise functions in python

# Importing modules
import os
import time

# Defining functions

def clear_screen():
    os.system("clear")
    return None

def display_dots():
    print(f"Progressing...")
    time.sleep(6)
    return None

def welcome_msg():
    print(f"Welcome to python scripting course")
    print(f"Let's start!")
    return None

def interval_msg():
    print(f"We have now reached to the middle of the course.")
    print(f"Let's continue")
    return None

def farewell_msg():
    print(f"Congratulations, you have completed the complete course")
    print(f"Course will end now! See you again :)")
    return None

# Calling the functions to constitute the workflow

clear_screen()
welcome_msg()
display_dots()
clear_screen()
interval_msg()
display_dots()
clear_screen()
farewell_msg()

