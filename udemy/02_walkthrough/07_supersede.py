#!/usr/bin/env python3

# This script is to demonstrate mentioning an interpreter in shebang line but calling script using another interpreter
# We'll see and document our results

print(f"Hello World!")

# If we call script on linux machine by ./07_supersede.py it gets interpreted by python3 mentioned in shebang line without error.
# However, if we try python 07_supersede.py, it gets executed using python2 and fails
# On our linux machine, python is sym link to python2
# python2 doesn't know formatting in print statement.
# So, interpreter mentioned on CLI while executing script supersedes interpreter mentioned in shebang line
