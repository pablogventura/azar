import random
negros = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

def fib(n):
    r=[0,1,1,1,2,3,4,6,9,14,21,31,47,70,105,158,237,355]
    if n in range(len(r)):
        return r[n]
    else:
        raise ValueError("sucecion fuera del limite")

def jugada():
    return random.random() <= 18/37.0

def partida(inicial, final):
    creditos = inicial
    apuesta = 1
    succ=1
    while True:
        numero = random.randint(0,36)
        if 1<=numero and numero<=18:
            creditos += apuesta
            succ=1
            apuesta = fib(succ)
        else:
            creditos -= apuesta
            succ+=1
            apuesta = fib(succ)
        if apuesta > 400 or creditos - apuesta < 0:
            return 0
        if creditos >= final:
            return 1

def probabilidad(final):
    return sum(partida(1000,final) for x in xrange(500))/float(500)

    
import matplotlib.pyplot as plt
import numpy as np

t = range(1100,3000,50)
print probabilidad(2000)
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
