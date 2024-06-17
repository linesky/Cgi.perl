import sys



def readstdin(arg1:int):
   ss=[]
   ii=0
   for s1 in sys.stdin:
       ss=ss+[s1]
   ii=len(ss)
   for s1 in range(ii):
        iii=ii-1-s1
        print(ss[iii])
    

    
print("\x1b[43;37m")
if 0==0:
    readstdin(0)





