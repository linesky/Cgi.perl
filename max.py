import sys
global counters
counters:float=0
def splitss(s:str):
    global counters
   
    if 0==0:

        try:
            ff:float=float(s)
            if counters==None:
                
                counters=ff
            if ff>counters:
                counters=ff
        except:
            a=0
    
        


def readstdin(arg1:int):
    global counters
    counters=None
    for s in sys.stdin:    
        splitss(s.strip())
    print(str(counters))

    
print("\x1b[43;37m")
if 0==0:
    readstdin(0)





