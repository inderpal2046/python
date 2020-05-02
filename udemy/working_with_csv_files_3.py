#!/usr/bin/env python3

# to read csv data and differentiate each row's columns without using csv module

req_file="/home/inderpal2406/tmp/data.csv"
fo=open(req_file,"r")
data=fo.readlines()
for i in data:
    print(i.strip("\n").split(","))
fo.close()

# for loop can be included after fo.close() also.
