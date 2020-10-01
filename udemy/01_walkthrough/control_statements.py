#!/usr/bin/env python3

# Suppose I have a list of paths
# Amongst them, I need to print the first path containing httpd

list_of_paths=['/root','/tmp','/home/user1','/etc/httpd','/var/log','/var/httpd']
print(f"The list of paths is : {list_of_paths}")
for i in list_of_paths:
    if 'httpd' in i:
        print(f"First occurence of httpd in list of paths is : {i}")
        break
print(f"End of script")


# break with while loop
count=1
while True:
    print(count)
    count+=1
    if count>10:
        break
print("End of while loop")
# Above logic can be simply put as while count<10 but to understand break, we have done it in above way


# printing first 10 numbers
print(f"Printing first 10 numbers:")
for i in range(11):
    print(i)


# printing first 10 numbers except 7
print(f"Printing first 10 numbers except 7:")
for i in range(11):
    if i==7:
        continue
    print(i)
