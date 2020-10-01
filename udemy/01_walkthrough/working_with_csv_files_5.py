#!/usr/bin/env python3

# creating list of all rows in csv file

import csv
import os

os.system("clear")

req_file="/home/inderpal2406/tmp/data.csv"
fo=open(req_file,"r")
data=csv.reader(fo)
list_of_data=list(data)		# or list_of_data=list(csv.reader(fo))
#print(list_of_data)
print(f"Header of csv file is as below, \n{list_of_data[0]} \n")		# to print first row or header of csv file
print(f"Total no. of rows in csv file are : {len(list_of_data)-1}")		# header is not considered as a row of data
