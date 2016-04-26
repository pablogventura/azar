import random




def jugar(credito, esperado):
    docena = 4
    trece = 1
    dnueve = 6

    while True:
        salio = random.randint(0,37)
        if 1 <= salio and salio <= 12:
            #docena paga 3
            credito += docena * 2
            docena = 4
            trece = 1
            dnueve = 6
        elif salio in [13,14,15]:
            #de a tres paga 12
            credito += trece * 11
            docena = 4
            trece = 1
            dnueve = 6
        elif 19 <= salio and salio <= 36:
            #paga 2
            credito += dnueve
            docena = 4
            trece = 1
            dnueve = 6
        else:
            credito -= docena
            credito -= trece
            credito -= dnueve
            docena *= 12
            trece *= 12
            dnueve *= 12
        if credito >= esperado:
            return 1
        if credito - docena - trece - dnueve <= 0:
            return 0
        

def probabilidad(esperado):
    juegos = [jugar(500,esperado) for i in range(2000)]
    return sum(juegos)/float(len(juegos))

import matplotlib.pyplot as plt
import numpy as np

t = range(550,5000,200)
s = [probabilidad(x) for x in t]
plt.plot(t, s)

plt.xlabel('Plata')
plt.ylabel('Probabilidad')
plt.title('Ganancias')
plt.grid(True)
plt.savefig("test.png")
plt.show()

