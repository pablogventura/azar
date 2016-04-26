import random
negros = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
def makro(n):
    if n>1:
        return 2**(n+1)
    else:
        return 1
    lista = [0,1,3,7,15,32,66,135,270]
    if n in range(len(lista)):
        return lista[n]
    else:
        return 0

def partida(topemaximo):
    succ = 1
    apuesta = makro(succ)
    creditos=1100
    while True:
        salio = random.randint(0,36)
        if salio in negros and salio%2==0 and salio!=0:
            creditos += apuesta * 2
            succ = 1
            apuesta = makro(succ)
        elif (salio in negros or salio%2==0) and salio!=0:
            apuesta = makro(succ)
        else:
            creditos -= apuesta * 2
            succ += 1
            apuesta = makro(succ)
        if creditos - apuesta <= 0:
            return 0
        if apuesta > 400:
            return 0
        if creditos >= topemaximo:
            return 1
        if creditos <= 0:
            return 0
        
def probabilidad(final):
    return sum(partida(final) for x in xrange(2000))/float(2000)

    
import matplotlib.pyplot as plt
import numpy as np

t = range(1100,3000,50)
s = []
for i,x in enumerate(t):
    print float(i)/len(t)
    s.append(probabilidad(x))
plt.plot(t, s)

plt.xlabel('Plata')
plt.ylabel('Probabilidad')
plt.title('Ganancias')
plt.grid(True)
plt.savefig("test.png")
plt.show()
