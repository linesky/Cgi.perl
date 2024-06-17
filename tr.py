import sys

def readstdin(arg1:str,arg2:str):

    for s1 in sys.stdin:
        s1=s1.replace("\\n", "\n")
        s1=s1.replace("\\t", "\t")
        s1=s1.replace("\\s", " ")
        s1=s1.replace("\\r", "\r")
        s1=s1.replace(arg1,arg2)
        print(s1)
    
 
    

    
print("\x1b[43;37m")
if len(sys.argv)>2:
    readstdin(sys.argv[1],sys.argv[2])





