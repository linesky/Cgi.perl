import sys


def readstdin(arg1:str,arg2:str):

    for s1 in sys.stdin:
        s1=s1.replace(arg1,arg2)
        if 0==0:
            print(s1)
    

    
print("\x1b[43;37m")
if len(sys.argv)>2:
    readstdin(sys.argv[1],sys.argv[2])





