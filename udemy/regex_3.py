#!/usr/bin/env python3

import os
import re

os.system("clear")

def initiate():
    print()
    print(f"text : {text}")

text="This is pythonnnnn and pythonnnnnnnnnn is easy"
initiate()
pattern=r"\bpython{3}\b"
print(re.findall(pattern,text))

initiate()
pattern=r"\bpython{3}"
print(re.findall(pattern,text))

initiate()
pattern=r"\bpython{10}\b"
print(re.findall(pattern,text))

initiate()
pattern=r"n{5}"
print(re.findall(pattern,text))

text="xaz xaaz xaaaz xaaazz xaaaaz xaaaaaz xaaaaaaz xaaaaaaaz"
initiate()
pattern=r"\bxa{2,5}z\b"
print(re.findall(pattern,text))

initiate()
pattern=r"\bxa{2,}z\b"
print(re.findall(pattern,text))

initiate()
pattern=r"\bxa{1,}z\b"
print(re.findall(pattern,text))

initiate()
pattern=r"\bxa+z\b"
print(re.findall(pattern,text))

text="xz xaz xxaz xaaz xaaaz"
initiate()
pattern=r"\bxa*z\b"
print(re.findall(pattern,text))

initiate()
pattern=r"\bxa?z\b"
print(re.findall(pattern,text))

initiate()
pattern=r"\bxa{0,1}z\b"
print(re.findall(pattern,text))
