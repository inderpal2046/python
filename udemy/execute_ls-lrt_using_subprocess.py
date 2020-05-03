#!/usr/bin/env python3

import subprocess
cmd="ls -lrt"
#sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)	# this produces output as byte code
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
print(f"The return code is : {rc}")
#print(f"Output is as below : \n{out}")		# prints output as string 
#print(f"Error is : \n{err}")			# prints error as string
# Suppose we don't want to print output as string, but instead as a list
print(f"Output is as below : \n{out.splitlines()}")		# splitlines() by default takes separator as \n
print(f"Error is as below : \n{err.splitlines()}")		# splitlines("\t") will consider \t as separator
