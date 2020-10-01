#!/usr/bin/env python3

name="  Inderpal    "
print(name)
print(f"{name.strip()}")

name="  Inderpal  Singh    Saini    "
print(f"{name}")
print(f"{name.strip()}")

name="python"
print(f"{name}")
print(f"{name.strip('p')}")
print(f"{name.strip('n')}")
print(f"{name.strip('t')}")

string="Python scripting is easy"
print(f"{string.strip('easy')}")

string="Python scripting is easy Python"
print(f"{string.strip('Python')}")
print(f"{string.lstrip('Python')}")
print(f"{string.rstrip('Python')}")

x="inder./i"
x=x.strip('./i')
print(x)

x="pythonyy"
print(f"{x.strip('p').strip('y')}")
print(f"{x.strip('p').lstrip('y')}")
print(f"{x.strip('p').rstrip('y')}")

# split operations

x="Python is easy."
print(f"{x.split()}")
print(f"{x.split('is')}")

x="Python is easy and is very popular."
print(f"{x.split('is')}")
