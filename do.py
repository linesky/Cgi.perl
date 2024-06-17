#!/usr/bin/python3
import subprocess
import sys
def readstdin(arg1:str,arg2:str):

    for n in sys.stdin:
        subprocess.run([arg1 ,arg2 ,n.strip()])
    

    
print("\x1b[43;37m")
if len(sys.argv)>2:
    readstdin(sys.argv[1],sys.argv[2])





