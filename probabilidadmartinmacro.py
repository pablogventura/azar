import random

def makro(n):
    lista = [0,1,3,7,15,32,66,135,270]
    if n in range(len(lista)):
        return lista[n]
    else:
        return 0

def jugada():
    return random.random() <= 18/37.0

def partida(inicial, final):
    creditos = inicial
    apuesta = 1
    succ=1
    while True:
        gane = jugada()
        if gane:
            succ=1
            creditos += apuesta
            apuesta = makro(succ)
        else:
            succ+=1
            creditos -= apuesta
            apuesta = makro(succ)
            if creditos - apuesta < 0:
                return 0
        if creditos >= final:
            return 1

def probabilidad(final):
    return sum(partida(1100,final) for x in xrange(2000))/float(2000)

    
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

t = range(1100,3000,50)
s = []
for i,x in enumerate(t):
    print float(i)/len(t)
    s.append(probabilidad(x))
fit_alpha, fit_loc, fit_beta=stats.gamma.fit(s)
print (fit_alpha, fit_loc, fit_beta)
plt.plot(t, s)

plt.xlabel('Plata')
plt.ylabel('Probabilidad')
plt.title('Ganancias')
plt.grid(True)
plt.savefig("test.png")
plt.show()
