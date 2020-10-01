#!/usr/bin/env python3

content_list=["Line 1","Line 2","Line 3","Line 4","Line 5"]
fo=open("line.txt","w")
for i in content_list:
    fo.write(i+"\n")
fo.close()
