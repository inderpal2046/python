#!/usr/bin/env python3

# read a csv file using readlines() function of file object (cursor position)

req_file="/home/inderpal2406/tmp/data.csv"
fo=open(req_file,"r")
data=fo.readlines()
fo.close()
for i in data:
    print(i.strip("\n"))

# But this prints line as rows only and colums are not separated.
