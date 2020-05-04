#!/usr/bin/env python3

# Script to check java version of system using python

import subprocess

cmd=["java","-version"]
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()

if rc==0:
#   print(err)
#   print(err.splitlines())
    for i in err.splitlines():
        if "version" in i:
            print(i.split()[2])
else:
    print(out)
