#!/usr/bin/env python3

import os
cmd="date"
status=os.system(cmd)
if status==0:
    print(f"Command executed successfully")
else:
    print(f"Command failed")
