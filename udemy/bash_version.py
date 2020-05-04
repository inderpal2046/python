#!/usr/bin/env python3


# importing module
import subprocess


# code to execute OS command using subprocess module
#cmd="bash --version"
#cmd_list=cmd.split()
cmd=["bash","--version"]
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stdin=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()		# useful to wait when we execute ssh commands
out,err=sp.communicate()


'''
# code to print only 4.4.2 bash version
if rc==0:
#   print(f"Command is successful and output is as below: \n{out.splitlines()}")	# splitlines() to convert string output to list
    op_list=out.splitlines()
    for i in list(range(len(op_list))): 
        print(f"{op_list[i]}")
else:
    print(f"Command failed and error is as below: \n{err}")
'''


# alternate logic for above code
if rc==0:
    for i in out.splitlines():
        if "version" in i and "release" in i:		# print only those lines which have version and release in them
#           print(i.split())				# split on basis of space and store in form of list
#           print(i.split()[3])
            print(i.split()[3].split("(")[0])
else:
    print(f"Command failed and error is as below: \n{err}")
    
