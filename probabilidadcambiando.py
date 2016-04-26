import random

def jugada():
    return random.random() <= 18/37.0

def partida(inicial, final):
    creditos = inicial
    apuesta = 1
    apos = True
    while True:
        if creditos % 100 == 0:
            apos = not apos
        gane = jugada()
        if gane == apos:
            creditos += apuesta
            apuesta = 1
        else:
            creditos -= apuesta
            apuesta *= 2
            if apuesta > 400 or creditos - apuesta < 0:
                return 0
        if creditos >= final:
            return 1

def probabilidad(final):
    return sum(partida(550,final) for x in xrange(2000))/float(2000)

    
import matplotlib.pyplot as plt
import numpy as np

t = range(550,2000,50)
s = [probabilidad(x) for x in t]
plt.plot(t, s)

plt.xlabel('Plata')
plt.ylabel('Probabilidad')
plt.title('Ganancias')
plt.grid(True)
plt.savefig("test.png")
plt.show()
