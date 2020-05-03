#!/usr/bin/env python3

# reading json data using json module

import json
req_file="/home/inderpal2406/tmp/file_1.json"
fo=open(req_file,"r")
#print(fo.read())	# read json data as string, but at a time we can read data only once, if I perform json.load() after this, error
print(json.load(fo))
#print(json.load(fo).get("glossary"))	# performing dictionary operation, this throws error if above statement is not commented
fo.close()
