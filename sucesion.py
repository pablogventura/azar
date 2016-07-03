import math

def ff(p):
    r= math.ceil(p/26.0)
    if r == p/26.0:
        r+=1
    return r
s=1
perdidas=0
n=1
lista = []
while s<=1000:
    lista.append(s)
    print "Nivel %s = %s" % (n,s)
    perdidas+=s
    n+=1
    s= int(ff(perdidas))
    
print lista
