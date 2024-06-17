import subprocess
import sys
def readstdin(arg1,arg2,arg3):
    arg11=arg1.replace("false","False")
    arg11=arg11.replace("true","True")
    
    arg111=bool(eval(arg11))
    
    if arg111:
        subprocess.run([arg2,arg3])
    

    
print("\x1b[43;37m")
if len(sys.argv)>3:
    readstdin(sys.argv[1],sys.argv[2],sys.argv[3])





