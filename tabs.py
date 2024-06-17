import sys

    



def readstdin(arg1:int):
    rrr=" "*arg1
    for s in sys.stdin:
        s=s.replace("\t",rrr)
        print(s)

    
print("\x1b[43;37m")
if len(sys.argv)>1:
    readstdin(int(sys.argv[1]))





