#
# Utility functions to inspect object attributes (QQ), to print the eval of expressons (AA)
#

EE = "\U0001F620" # 😠 "E"moji (larger than 1-ASCII string in print size) <= chcp 65001 for utf-8 ??
SS = lambda s, L: s if len(s) <= L else (s[:(L-2)]+EE); # "S"hortend string (witin Limit, L)
#
# Printing Emoji has problem on Windows 10, not because of interpreter (c:\Windows\System32\cmd.exe), but because of terminal (c:\Windows\System32\conhost.exe).
#                                
# <UTF-8 support>  Console   Terminal 
# Command Prompt      No          Yes       https://github.com/microsoft/terminal  
# PowerShell          No          Yes       https://learn.microsoft.com/en-us/windows/terminal/install 
#
# CTRL + ',' (with terminal.exe) to customize "Profiles" including "Starting directory".
#

def QQ(o): [print("%04d:%20s:%100s"%(i,a,SS(str(getattr(o,a)),100))) for (i,a) in enumerate(dir(o),1)] # "Q"uery for obj attr
def AA(e): print(e+" ==> "+str(eval(e))); # "A"nswer for str expression
def ZZ(): print("*"*126) # "ZZ" is the long-line marking
#
# Q,W,E;A,S;Z,X are chosen because they are close to each other in qwerty !
# Then they are doubled to avoid "unintented-namimg-override" !
#

def XX(o,a): # to check the e"X"cesivevly long Object's Attribute
    r=getattr(o,a);s=str(r); 
    print("\n"+"type of "+a+"="+str(type(r))+"\n");
    print("\n"+"leng of "+a+"="+str(len(s))+"\n");      
    return getattr(o,a)

def WW(NAMESPACE = globals()):   # "W"ord-wide checking variables in globals() NAMESPACE 
  for name in NAMESPACE.keys():
    v = NAMESPACE[name] # <==> v = eval(name,NAMESPACE); # <== globals(), locals()
    print("%-20s:%-20s:%-100s"%(SS(name,20),SS(str(type(v))[8:-2],20),SS(str(v),100)))

import os
import sys

if __name__ == "__main__":
    ZZ()
    AA("os.getcwd()")
    AA("sys.version")

    ZZ()
    QQ(QQ)
    ZZ()
    QQ(AA)

    g1 = XX(QQ, '__globals__')
    g2 = XX(AA, '__globals__')

    WW()
