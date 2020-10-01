#!/usr/bin/env python3

import re

text="This $ is python _ and it is easy to - learn. Python2 Python3 44"
pattern="is"	# pattern which we want to search or operate upon
print(re.findall(pattern,text))	# will print is thrice in a list, it finds is in This as well
print(re.findall("is","This is python and it is easy to learn."))	# not a good practice, instead store pattern and text in variables
print(len(re.findall(pattern,text)))	# to check no. of occurrences of pattern, as output is in form of list, len() can be used
pattern="i[st]"
print(re.findall(pattern,text))
print(len(re.findall(pattern,text)))
pattern="a"
print(re.findall(pattern,text))
print(len(re.findall(pattern,text)))
pattern="a"
print(re.findall(pattern,text))
pattern="[aet]"
print(re.findall(pattern,text))
pattern="[Tt]"
print(re.findall(pattern,text))
pattern="\w"
print(re.findall(pattern,text))
pattern="\w\w"
print(re.findall(pattern,text))
pattern="\w\w\w"
print(re.findall(pattern,text))
pattern="\W"
print(re.findall(pattern,text))
pattern="\d"
print(re.findall(pattern,text))
pattern="\d\d"
print(re.findall(pattern,text))
pattern="\d\d\d"
print(re.findall(pattern,text))
pattern="Python\d"
print(re.findall(pattern,text))
pattern="Python\d\d"
print(re.findall(pattern,text))
pattern="Python2"
print(re.findall(pattern,text))
pattern="Python[23]"
print(re.findall(pattern,text))
pattern="."
print(re.findall(pattern,text))
pattern=".."
print(re.findall(pattern,text))
pattern="..."
print(re.findall(pattern,text))
pattern="\."
print(re.findall(pattern,text))
text="IP address of apache server is : 10.10.16.19  3628292903"
pattern="\d\d\.\d\d\.\d\d\.\d\d"
print(re.findall(pattern,text))
pattern="\d\d.\d\d.\d\d.\d\d"  # matches extra digits as well if present
print(re.findall(pattern,text))
#pattern="\w\w.\w\w.\w\w.\w\w"	# gives undesired output, fetches additional output as a match
pattern="\w\w\.\w\w\.\w\w\.\w\w"
print(re.findall(pattern,text))
