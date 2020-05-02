#!/usr/bin/env python3

# read data from csv file using csv module to separate columns in each row

import csv
req_file="/home/inderpal2406/tmp/data.csv"
fo=open(req_file,"r")
data=csv.reader(fo)
for i in data:
    print(i)
fo.close()
