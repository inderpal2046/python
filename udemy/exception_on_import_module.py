#!/usr/bin/env python3

# Script will handle error of importing a non-default python module

try:
    import xlrd
except Exception as error:
    print(error) 

# This script can be further enhanced to as user that which module needs to be tested if present or not.
# If not then handle the exception and install the module.
