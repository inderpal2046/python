#!/usr/bin/env python3

content_list=["Inderpal Singh","Omkar Solaskar","Sarab Anand"]
fo=open("friends.txt","a") 
for i in content_list:
    fo.write(i+"\n")
fo.close()
