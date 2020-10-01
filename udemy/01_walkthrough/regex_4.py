#!/usr/bin/env python3

# Fourth script to explain RegEx examples

import os
import re

os.system("clear")

def initiate():
    print()
    print(f"text : {text}")

text="this is python This is good thIs is not bad"
initiate()
pattern=r"\bthis\b"				# search this anywhere/wherever it appears
print(re.findall(pattern,text,re.IGNORECASE))  	# or print(re.findall(pattern,text,re.I))

text="""this is first line
This is second line
thIs is third line
this is fourth line
this is last line"""
initiate()
#pattern=r"\bthis\b"
#print(re.findall(pattern,text))	# prints all occurrences of this
pattern=r"\b^this\b"			# search for this and print it wherever it appears in the beginning
#print(re.findall(pattern,text))	# will print only one this as ^ looks for this at the start of the multiline string
#print(re.findall(pattern,text,re.MULTILINE))	# will look for ^this in all lines of multiline string
#print(re.findall(pattern,text,re.MULTILINE|re.IGNORECASE))
print(re.findall(pattern,text,re.M|re.I))	# same as above

text="""this is first line enD
This is second line End
thIs is third line
this is fourth line 
this is last line end"""
initiate()
pattern=r"\bend$\b"			# search for end and print it wherever it appears in the end
#print(re.findall(pattern,text))	# output is end as $ will print the search at the end of the multiline string
#print(re.findall(pattern,text,re.M))	# same output as above
print(re.findall(pattern,text,re.M|re.I))
