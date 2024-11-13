import os
import sys

def a(o): [print("%04d:%20s:%s"%(i,a,getattr(o,a)) for (i,a) in enumerate(dir(o),1))]  
def v(e): print(e+" ==> "+str(eval(e)));

print("_______")
v("os.getcwd()")
v("sys.version")
