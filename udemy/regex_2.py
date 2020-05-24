#!/usr/bin/env python3

# Script 2 to practise RegEx (Regular Expressions)

import re
import os

os.system("clear")

def initiate():
    print()
    print(f"text : {text}")

text="it is a python and learn it is easy to learn"
initiate()
print("Working with '^i[st]'")
pattern="^i[st]"
print(re.findall(pattern,text))

initiate()
print("Working with 'learn$'")
pattern="learn$"
print(re.findall(pattern,text))

text="learn python and learnAWS, AWSlearn it'll be great to learn"
initiate()
print("Working with '\\blearn'")
pattern=r"\blearn"
print(re.findall(pattern,text))

initiate()
print("Working with 'learn\\b'")
pattern=r"learn\b"
print(re.findall(pattern,text))

initiate()
print("Working with '\\blearn\\b'")
pattern=r"\blearn\b"
print(re.findall(pattern,text))

text="learn python learn and learnAWS, AWSlearn it'll islearnthe be great to learn"
initiate()
print("Working with '\\Blearn'")
pattern=r"\Blearn"
print(re.findall(pattern,text))

initiate()
print("Working with 'learn\\B'")
pattern=r"learn\B"
print(re.findall(pattern,text))

initiate()
print("Working with '\\Blearn\\B'")
pattern=r"\Blearn\B"
print(re.findall(pattern,text))

text="learn python	and \t automate		the stuff"
initiate()
print("Working with '\\t'")
pattern=r"\t"
print(re.findall(pattern,text))

text="learn python	and \n automate	the stuff"
initiate()
print("Working with '\\n'")
pattern=r"\n"
print(re.findall(pattern,text))
