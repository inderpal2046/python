#!/usr/bin/env python3

# defining a set

set1={9,4,8,5,1,0}
print(set1)

# defining a set with duplicate values
print()
set2={3,4,1,9,5,3,0,4,2}
print(set2)

# boolean of set

print()
set1=set({})	# defining an empty set
set2={1,2,3,4}
print(f"Boolean of an empty set is : {bool(set1)}")
print(f"Boolean of non-empty set is : {bool(set2)}")

# list to set conversion

print()
mylist=[3,2,7,6,3,4]
myset=set(mylist)
print(f"The list is : {mylist}")
print(f"The set is : {myset}")

# operations on set

print()
print(f"Below operations can be performed on a set: \n{dir(myset)}")

# union and intersection operation

print()
a={1,2,3,4,5}
b={4,5,6,7}
print(f"Set a is : {a}")
print(f"Set b is : {b}")
print(f"a union b is : {a.union(b)}")
print(f"a intersection b is : {a.intersection(b)}")
