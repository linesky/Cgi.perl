import sys



def readstdin(arg1:int):

    counters:float=0
    
    for s1 in sys.stdin:
        try:
            ff:float=float(s1)
            counters+=ff
            print(str(counters)+"\t=\t"+s1)
        except:
            a=0
    

    
print("\x1b[43;37m")
if 0==0:
    readstdin(0)





