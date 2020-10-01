#!/usr/bin/env python3

# define tuple

mytuple=()	# empty tuple
yourtuple=(1,2,3)	# non-empty tuple

# printing tuple

print(mytuple)
print(yourtuple)

# boolean conversion of tuple

print(f"Boolean of an empty tuple is : {bool(mytuple)}")
print(f"Boolean of non-epmty tuple is : {bool(yourtuple)}")

# list in a tuple

list_in_tuple=(1,2,[3,5.7,'inder'],8,90)
print(f"We can have a list as an element inside a tuple: {list_in_tuple}")

# accessing individual elements in tuple

mytuple=(1,2,[4,5.5,'inder'],99,88)
print(mytuple)
print(f"The first element in tuple is : {mytuple[0]}")
print(f"The last element in tuple is : {mytuple[-1]}")
print(f"The list element in tuple is : {mytuple[2]}")
print(f"Accessing second element of list within tuple : {mytuple[2][1]}")

# operations on tuple

mytuple=(1,2,3,4,5)
print(f"Operations that can be preformed on tuple : \n{dir(mytuple)}")

# count operation

mytuple=(1,2,3,4,5,3)
print(mytuple)
print(f"No of occurences of 3 : {mytuple.count(3)}")
print(f"No of occurences of 6 : {mytuple.count(6)}")

# index operation

print(f"Index value of 3 in mytuple is : {mytuple.index(3)}")
print(f"Next occurence of 3 after index 2 is at index: {mytuple.index(3,3)}")

# length of string, list and tuple

mystring="Inderpal"
mylist=[1,2,3,4,5]
mytuple=(1,2,3)
print(f"{mystring} \n{mylist} \n{mytuple}")
print(f"Length of string : {len(mystring)}")
print(f"Length of list : {len(mylist)}")
print(f"Length of tuple : {len(mytuple)}")

# print a range of values from tuple

mytuple=(1,2,3,4,5,6,7)
print(mytuple)		# complete tuple
print(mytuple[:])	# complete tuple
print(mytuple[0:])	# complete tuple
print(f"From index 2 till last : {mytuple[2:]}")
print(f"From index 0 to index 4 : {mytuple[:5]}")
print(f"From index 2 to index 4 : {mytuple[2:5]}")

# alternate way to define tuple

x=5	# integer
y=5,	# tuple with one value
z=5,6,7	# tuple with 3 values

print(x,type(x))
print(y,type(y))
print(z,type(z))
