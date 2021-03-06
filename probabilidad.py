import random

def jugada():
    return random.random() <= 18/37.0

def partida(inicial, final):
    creditos = inicial
    apuesta = 1
    while True:
        gane = jugada()
        if gane:
            creditos += apuesta
            apuesta = 1
        else:
            creditos -= apuesta
            apuesta *= 2
            if creditos - apuesta < 0:
                return 0
        if creditos >= final:
            return 1

def probabilidad(final):
    return sum(partida(1100,final) for x in xrange(2000))/float(2000)

    
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
