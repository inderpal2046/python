# OS independent python script to clear terminal and display content of current directory with intermittent delays.

# Importing modules
import os
import platform
import time

# Defining function
def myfunction(cmd1,cmd2):
    print(f"Clearing the terminal. Please wait...")
    time.sleep(2)
    os.system(cmd1)
    print(f"Displaying content of current directory. Please wait...")
    time.sleep(2)
    os.system(cmd2)

OS=platform.system()
if OS=="Linux":
    myfunction("clear","ls -l")
else:
    myfunction("cls","dir")
