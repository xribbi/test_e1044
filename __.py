#
# Utility functions to inspect object attributes (QQ), to print the eval of expressons (AA)
#

SS = lambda s, L: s if len(s) <= L else s[:L]+" "+">"*5+" excess "+"<"*5; # "S"hortend string (witin Limit, L)
def QQ(o): [print("%04d:%20s:%100s"%(i,a,SS(str(getattr(o,a)),100))) for (i,a) in enumerate(dir(o),1)] # "Q"uery for obj attr
def AA(e): print(e+" ==> "+str(eval(e))); # "A"nswer for str expression
def ZZ(): print("*"*126) # "ZZ" is the long-line marking
#
# Q,A,Z,S are chosen because they are close to each other in qwerty !
# Then they are doulbed to avoid "unintented-namimg-override" !
#

def qq(o,a):
    r=getattr(o,a);s=str(r); 
    print("\n"+"type of "+a+"="+str(type(r))+"\n");
    print("\n"+"leng of "+a+"="+str(len(s))+"\n");      
    return getattr(o,a)
#
# to check the "excesivevly" long Object's Attribute
#

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

    g1 = qq(QQ, '__globals__')
    g2 = qq(AA, '__globals__')
