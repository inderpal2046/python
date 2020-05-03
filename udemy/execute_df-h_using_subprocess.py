#!/usr/bin/env python3

import subprocess
#cmd="df -h".split()		# this automatically spits the string into a list based on space as separator
cmd=["df","-h"]
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
print(f"The return code is : {rc}")
#print(f"The output is as below : \n{out}")
#print(f"The error is as below : \n{err}")
# Suppose we don't want to print output as string, but instead as a list
print(f"Output is as below : \n{out.splitlines()}")		# splitlines() by default takes separator as \n
print(f"Error is as below : \n{err.splitlines()}")		# splitlines("\t") will consider \t as separator
