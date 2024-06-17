import sys
def splitss(s:str,i:int):
    sss=" "*i
    print(sss+s)



def readstdin(arg1:int):

    for ss in sys.stdin:
        splitss(ss,arg1)
    

    
print("\x1b[43;37m")
if len(sys.argv)>1:
    readstdin(int(sys.argv[1]))





