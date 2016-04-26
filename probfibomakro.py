import random
negros = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

def partida(topemaximo):
    succ = 1
    apuesta = fib(succ)
    creditos=1100
    while True:
        salio = random.randint(0,36)
        if salio in negros and salio%2==0 and salio!=0:
            creditos += apuesta * 2
            succ -= 2
            if succ <= 0:
                succ = 1
            apuesta = fib(succ)
        elif (salio in negros or salio%2==0) and salio!=0:
            apuesta = fib(succ)
        else:
            creditos -= apuesta * 2
            succ += 1
            apuesta = fib(succ)
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
s = [probabilidad(x) for x in t]
plt.plot(t, s)

plt.xlabel('Plata')
plt.ylabel('Probabilidad')
plt.title('Ganancias')
plt.grid(True)
plt.savefig("test.png")
plt.show()
