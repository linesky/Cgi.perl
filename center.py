import sys
def splitss(s:str,i:int):
    s=s.replace("\r","\n")
    s=s.replace("\n\n","\n")
    ss=s.split("\n")
    
    for s1 in ss:
        s1=s1.strip()
        t1=(((i//2)-(len(s1))//2))
        if t1<0:
            t1=0
        sss=" "*t1
        print(sss+s1)



def readstdin(arg1:int):

    
    for ss in sys.stdin:
        splitss(ss,arg1)
    
    

    
print("\x1b[43;37m")
readstdin(0)





