#!/usr/bin/env python3

# This script will check if java version on host is a valid java version or not
# Logic used is based on membership operator
# For, now the host java version is being assumed using a hard-coded value.
# Later this script can be modified, when we learn how to find java version on host using python

'''
valid_java_versions=['1.6','1.7','1.8','1.9']
host_java_version='1.8'

if host_java_version in valid_java_versions:
    print(f"Host deployed with correct java version.")
else:
    print(f"Host deployed with incorrect java version.")
'''

# Similarly, we can check if a user is authorized to start a db or not

valid_db_users=['db_admin','db_boss','db_master']
current_user='db_boss'

if current_user in valid_db_users:
    print(f"{current_user} is authorized to start the DB.")
else:
    print(f"{current_user} is not authorized to start the DB.") 
