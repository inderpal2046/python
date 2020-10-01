#!/usr/bin/env python3

# print json data using normal method of reading data. This prints the json object as a string.

import json
req_file="/home/inderpal2406/tmp/file_1.json"
fo=open(req_file,"r")
data=fo.read()
print(data)
fo.close()

# but we want to interpret the key-value pairs and not print json file as it is.
# check working_with_json_files_2.py
