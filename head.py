import sys
def splitss(s:str):
    print(s)



def readstdin(arg1:int):
    ii=0

    for ss in sys.stdin:
        if ii < arg1:
            splitss(ss)
        ii+=1

    
print("\x1b[43;37m")
if len(sys.argv)>1:
    readstdin(int(sys.argv[1]))





