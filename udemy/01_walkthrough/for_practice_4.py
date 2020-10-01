#!/usr/bin/env python3


# to use for loop to fetch each character in the string
my_name="Inderpal Singh Saini"
for i in my_name:
    print(i)


# to use join function to fetch each character in the string
print(f"{':'.join(my_name)}")


# for loop over a list
my_list=[1,2,3,4,5]
print(f"my_list={my_list}")
for i in my_list:
    print(i)


# for loop over a tuple
my_tuple=(1,2,3,4,5)
print(f"my_tuple={my_tuple}")
for i in my_tuple:
    print(i)


# for loop over a list which has tuple as elements in it
list_with_tuple=[(1,2),(3,4),(5,6)]
for i in list_with_tuple:
    print(f"{i}")


# to unpack each value from tuple which is element in list
list_with_tuple=[(9,8),(7,6),(5,4)]
print(f"List with tuple is : {list_with_tuple}")
for x,y in list_with_tuple:
    print(f"x={x}  y={y}")


# for loop in a dictionary
my_dict={'a':1,'b':2,'c':3}
print(f"my_dict={my_dict}")
for i in my_dict:
    print(f"{i}")	# will print only keys in the dictionary


# for loop over my_dict.keys() function
print(f"The keys in the dictionary are:")
for i in my_dict.keys():
    print(i)		# will print key values


# for loop over my_dict.values() function
print(f"The values in the dictionary are:")
for i in my_dict.values():
    print(i)		# will print only values of keys


# for loop over each item in the dictionary, an item is combination of a key-value pair in a dictionary
# by default my_dict.items() function will produce output as a list of key-value pairs as tuple
print(f"Each item in the dictionary is:")
for i in my_dict.items():
    print(i)


# for loop to fetch keys in the dictionary using items() function of the dictionary
print(f"Keys using items() function:")
for i,j in my_dict.items():
    print(i)

print(f"Values using items() function:")
for i,j in my_dict.items():
    print(j)

print(f"Key and values using items() function:")
for i,j in my_dict.items():
    print(i,j) 
