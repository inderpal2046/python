#!/usr/bin/env python3

# join operations

x="python"
print(x)
print(" ".join(x))
print("-".join(x))
print("^".join(x))
print(":".join(x))
print("\n".join(x))
print("\t".join(x))
print(f"{' '.join(x)}")

# center operations

name_1="Inderpal"
name_2="Inderpal Singh"
name_3="Inderpal Singh Saini"
print(f"{name_1.center(50)}")
print(f"{name_2.center(50)}")
print(f"{name_3.center(50)}")

# zfill

name="inder"
print(f"{name.zfill(10)}")
