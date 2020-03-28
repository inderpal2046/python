#!/usr/bin/env python3

# defining an empty dictionary

mydict={}	# an empty dict
print(mydict,type(mydict))

# boolean conversion of an empty dict

print(f"Boolean of empty dict is : {bool(mydict)}")

# defining non-empty dict

mydict={'flower':'lotus','vegetable':'carrot','number':44,1:'one','two':2}
print(mydict)

# boolean of non-empty dict

print(f"Boolean of non-empty dict is : {bool(mydict)}")

# accessing values within dict

print(mydict['vegetable'])
print(mydict.get('number'))

# accessing non-existent key from dict

#print(mydict['three'])  # commented as this way gives error while retrieving a non-existent key
print(mydict.get('three'))

# operations on dict

print(f"Below operations can be performed on a dict : \n{dir(mydict)}")

# clearing operation

print(mydict)
print(f"We'll now clear our dict.")
mydict.clear()
print(mydict)

# adding key-value pairs to dict

mydict={'Name':'Inderpal Singh','Last name':'Saini','age':26}
print(mydict)
mydict['gender']="male"
print(mydict)
mydict['gender']="female"
print(mydict)

# printing only keys of dict

print(mydict)
print(f"The keys in dict are : {mydict.keys()}")

# printing only values of dict

print(mydict)
print(f"The values in dict are : {mydict.values()}")

# printing dict items

print(mydict)
print(f"The items in dict are : {mydict.items()}")

# copy operation

print(mydict)
print(f"Creating copy of mydict by direct assigment...")
copy1=mydict
print(f"Memory locations of original dict and copy dict : {id(mydict)} \t {id(copy1)}")
print(f"creating copy of mydict using copy operation...")
copy2=mydict.copy()
print(f"Memory locations of original dict and copy dict : {id(mydict)} \t {id(copy2)}")

# update operation

print()
print(f"Update operation - add one dict to another")
print(f"Defining 2 dicts...")
dict1={'Country':'India','State':'Maharashtra'}
dict2={'City':'Mumbai'}
print(f"Dictionary 1 : {dict1}")
print(f"Dictionary 2 : {dict2}")
print(f"Updating dict 1 with dict 2...")
dict1.update(dict2)
print(f"Dict 1 after update : {dict1}")

# pop operation

print()
print(f"Pop operation - helps to remove key-value pair from dict by specifying the key name")
dict1={'Country':'India','State':'Maharashtra'}
print(dict1)
print(f"Popping 'Country' key...")
dict1.pop('Country')
print(f"After pop operation dict1 is : {dict1}")

# popitem operation

print()
print(f"Popitem operation - helps to remove key-value pair from dict without specifying the keyname")
print(f"Popitem operation removes key-value pair randomly, though in our case all itema were popped from last.")
print(f"Popitem operation doesn't accept any argument.")
dict1={'Country':'India','State':'Maharashtra','City':'Mumbai','Node':'Nerul'}
print(f"Dict is : {dict1}")
print(f"Performing one popitem operation...")
dict1.popitem()
print(f"New dict : {dict1}")
print(f"Performing second popitem operation...")
dict1.popitem()
print(f"New dict : {dict1}")
print(f"Assigning the popped item to another new dict...")
print(f"Performing another popitem...")
dict2=dict1.popitem()
print(f"The new dict is : {dict1} and the popped item is : {dict2}") 

# fromkeys operation

print()
print(f"Defining keys as a list...")
keys=[1,2,3,4,5]
print(f"list of keys is : {keys}")
print(f"Assigning keys from list to dictionary...")
mydict=dict.fromkeys(keys)
print(f"The dict is : {mydict}")
print(f"Assigning individual values to keys in dict...")
mydict[1]="a"
mydict[2]="b"
print(f"After assigning values for 1 and 2 keys in dict : {mydict}")

# setdefault operation

print()
print("setdefault operation")
dict={'a':'None'}
print(f"The dict with none value is : {dict}")
print(f"Setting default value for key with None value...")
dict.setdefault('a','letter a')
print(f"New dict is : {dict}")

print()
dict={'a':'alphabet a'}
print(f"The dict with a value is : {dict}")
print(f"Setting default value for key with already existing value...")
dict.setdefault('a','letter a')
print(f"New dict is : {dict}")


print()
dict={'a':'alphabet a'}
print(f"The dict with a value is : {dict}")
print(f"Setting default value for key which doesn't exist...")
dict.setdefault('b','letter b')
print(f"New dict is : {dict}")
