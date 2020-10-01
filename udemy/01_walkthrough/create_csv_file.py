#!/usr/bin/env python3

# script to create a csv file

import csv

csv_filename="/home/inderpal2406/tmp/data_3.csv"

fo=open(csv_filename,"w",newline="")		# newline="" is to avoid extra newline in output when we open created csv file using excel
csv_writer=csv.writer(fo)			# csv.writer(fo,delimiter="|") if delimiter apart from , has to be used
csv_writer.writerow(["Sr.No","Name","Age"])
csv_writer.writerow([1,"Ram",23])
csv_writer.writerow([2,"Laxman",22])
csv_writer.writerows([[3,"Sita",23],[4,"Hanuman",20],[5,"Sughvir",24]])		# write all rows using one single command and list of lists
data=[[6,"Ravan",27],[7,"Bharat",23],[8,"Lav",8]]				# storing list of lists into a variable
csv_writer.writerows(data)
fo.close()

