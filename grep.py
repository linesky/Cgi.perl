import sys
def splitss(s:str):
    s2=s.find(sys.argv[1])
    if s2>-1:
        print(s)
        


def readstdin(arg1:int):

    for s1 in sys.stdin:
        splitss(s1)
    

    
print("\x1b[43;37m")
if 0==0:
    readstdin(0)





