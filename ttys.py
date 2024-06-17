import sys



def readstdin(i:int):
    ii=i-1
    for s1 in sys.stdin:
        if len(s1)<i:
            print(s1)
        else:
            while s1!="":
                if len(s1)<ii:
                    print(s1)
                    s1=""
                else:
                    print(s1[0:ii])
                    s1=s1[ii:]

    

    
print("\x1b[43;37m")
if len(sys.argv)>1:
    readstdin(int(sys.argv[1]))





