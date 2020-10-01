#!/usr/bin/env python3

# This script will accept password from user without displaying it on screen when user enters it.
# Later we display it just to verify what the usr entered.

import os
import getpass

os.system("clear")
password=getpass.getpass()
print(f"The password is {password}")
password=getpass.getpass(prompt="Enter DB password: ")
print(f"The password is {password}")
user=getpass.getuser()
print(f"The user is {user}")
