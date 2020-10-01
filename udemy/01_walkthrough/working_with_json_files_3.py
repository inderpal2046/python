#!/usr/bin/env python3

# writing data to json file

import json
my_dict={"Name":"Inderpal Singh","Skills":["Linux","Bash","AWS","Python"]}
req_file="/home/inderpal2406/tmp/file_2.json"
fo=open(req_file,"w")
#json.dump(my_dict,fo)	# this types data as dictionary in single line in the json file. This is also json data. But we need indentation.
json.dump(my_dict,fo,indent=4)	# indentation of 4 spaces
fo.close()
