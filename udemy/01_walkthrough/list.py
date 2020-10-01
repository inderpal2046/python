#!/usr/bin/env python3

# list operations

# conversion to boolean

mylist_1=[]
mylist_2=[1,2,3,55.78,'inder']
print(f"Boolean of an empty list is always {bool(mylist_1)}")
print(f"Boolean of a non-empty list is always {bool(mylist_2)}")

# printing a list

mylist=[88,92,77.62238,'Inderpal Singh']
print(f"The list data is : {mylist}")

# printing type of data structure as a list

print(f"type of 'mylist' data structure is : {type(mylist)}")

# print individual values of the list

print(f"First element in list is: {mylist[0]}")
print(f"Second element in list is: {mylist[1]}")
print(f"Last element in list is: {mylist[-1]}")
print(f"Second last element in list is: {mylist[-2]}")

# print individual character of a value in list, this will work for only string values in the string 

print(f"Second character in the string value of the list is: {mylist[-1][1]}")

# print a range of values of the list

print(f"The entire list is: {mylist}")
print(f"The entire list is: {mylist[:]}")
print(f"The entire list from index 1: {mylist[1:]}")
print(f"The entire list from index 0: {mylist[0:]}")
print(f"The list from index 1 and next 2 subsequent values : {mylist[1:4]}")
print(f"lists are mutable")
print(f"Changing value at index 0 in list")
mylist[0]=99
print(f"{mylist}")
print(f"Operations which can be performed on list are as follows,")
print(f"{dir(mylist)}")
print(f"Index of '92' value in list is: {mylist.index(92)}")
print(f"No. of occurence of 10 in list : {mylist.count(10)}")
print(f"Clearing the list now...")
mylist.clear()
print(f"After clear operation, the list is: {mylist}")
print(f"Since, the list is empty, its boolean equivalent is: {bool(mylist)}")
print(f"initializing the list again...")
mylist=[1,2,3,4,'inder']
print(f"The 'mylist' values are : {mylist}")
print(f"Making a copy of mylist at a different memory location using copy operation...")
newlist=mylist.copy()
print(f"The 'newlist values are : {newlist}")
print(f"memory location of 'mylist' is : {id(mylist)}")
print(f"Memory location of 'newlist' is : {id(newlist)}")
print(f"Appending 88 to our 'mylist'...")
mylist.append(88)
print(f"updated list is : {mylist}")
mylist.insert(2,1989)
print(f"Inserting 1989 value at index 2 in 'mylist' : {mylist}")
mylist.extend(newlist)
print(f"Extending mylist with values of newlist : {mylist}")
mylist.remove(3)
print(f"Removing 3 from 'mylist' : {mylist}")
mylist.pop()
print(f"Popping last value in mylist : {mylist}")
mylist.pop(3)
print(f"Popping index 3 in mylist : {mylist}")
print(f"What's being popped now : {mylist.pop()}")
print(f"After pop : {mylist}")
mylist.reverse()
print(f"Reversing the list: {mylist}")
print(f"Sort operation will work only on numeric values. If list has string values and we perform sort, it throws an error.")
mylist=[6,77,92,8.02,82]
print(mylist)
mylist.sort()
print(f"Sorted list is : {mylist}")
