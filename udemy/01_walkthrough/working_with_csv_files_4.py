#!/usr/bin/env python3

# to read csv data using csv reader and delimiter as | and not comma

import csv
req_file="/home/inderpal2406/tmp/data_2.csv"
fo=open(req_file,"r")
data=csv.reader(fo,delimiter="|")
for i in data:
    print(i)
fo.close()
