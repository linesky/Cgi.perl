from tkinter import *
from tkinter import messagebox

import sys
def splitss(s:str,i:int):
    if 0==0:
        
        print(s)
        


def readstdin(arg1:int):
    ii:int=0
    for ss in sys.stdin:
        splitss(ss,arg1)
        if ii>arg1:
            ii=0
            a=messagebox.showinfo("ok to continue","continue?")
        ii+=1
    

    
print("\x1b[43;37m")
root=Tk()
root.geometry("100x100")
root.config(bg="yellow")
if len(sys.argv)>1:
    readstdin(int(sys.argv[1]))





