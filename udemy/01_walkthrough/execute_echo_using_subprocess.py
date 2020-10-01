#!/usr/bin/env python3

import subprocess
#cmd="echo $HOME".split()
#cmd=["echo","$HOME"]
cmd="echo $HOME"
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
print(f"The return code is : {rc}")
print(f"The output is as below : \n{out}")
print(f"The error is as below : \n{err}")
