import os
import sys

SS = lambda s, L: s if len(s) <= L else s[:L]+" "+">"*5+" excess "+"<"*5; # "S"hortend string (witin Limit, L)
def QQ(o): [print("%04d:%20s:%100s"%(i,a,SS(str(getattr(o,a)),100))) for (i,a) in enumerate(dir(o),1)] # "Q"uery for obj attr
def AA(e): print(e+" ==> "+str(eval(e))); # "A"nswer for str expression
def LL(): print("*"*126) # "L"ong Line

LL()
AA("os.getcwd()")
AA("sys.version")

LL()
QQ(QQ)
LL()
QQ(AA)

