import random


def jugar_hasta(maximo):
    credito = 35
    antes = random.randint(0,36)
    while True:
        jugada = random.randint(0,36)
        if jugada == antes:
            credito -= 35
        else:
            antes = jugada
            credito += 1
        if credito >= maximo:
            return 1
        elif credito < 35:
            return 0

def probabilidad(valor):
    jugadas = [jugar_hasta(valor) for i in range(1000)]
    return sum(jugadas)/float(len(jugadas))
    
import matplotlib.pyplot as plt
import numpy as np

t = range(20,200)
s = [probabilidad(x) for x in t]
plt.plot(t, s)

plt.xlabel('Plata')
plt.ylabel('Probabilidad')
plt.title('Ganancias')
plt.grid(True)
plt.savefig("test.png")
plt.show()
