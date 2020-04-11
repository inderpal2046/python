#!/usr/bin/env python3

# This is a platform independent script to clear terminal

import os
import platform
import sys

OS=platform.system()

if OS=="Windows":
    os.system("cls")
elif OS=="Linux":
    os.system("clear")
else:
    print(f"OS couldn't be determined. Exiting script.")
    sys.exit(1)
