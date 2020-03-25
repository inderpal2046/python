#!/usr/bin/env python3

x="Python is easy and is very popular."
print(f"The string is : {x}")
print(f"No. of occurence of 'i' is : {x.count('i')}")
print(f"No. of occurence of 'is' is : {x.count('is')}")
print(f"No. of occurence of 'p' is : {x.count('p')}")

# index
print(f"{x.index('p')}")
print(f"{x.index('is')}")
print(f"{x.index('p',25)}")

# find
print(f"{x.find('p')}")
print(f"{x.find('is')}")
print(f"{x.find('p',25)}")
print(f"{x.find('z')}")
