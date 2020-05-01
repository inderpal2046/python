#!/usr/bin/env python3

content_list=["This is line 1.\n","This is line 2.\n","This is line 3.\n"]
fo=open("lines.txt","w")
fo.writelines(content_list)
fo.close()
