import random
negros = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

def fib(n):
    f= [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610]
    if n in range(len(f)):
        return f[n]
    else:
        raise ValueError("fibonacci mal")

def jugada():
    return random.random() <= 18/37.0

def partida(inicial, final):
    creditos = inicial
    apuesta1 = 1
    apuesta2 = 1
    apuesta3 = 1
    succ1=1
    succ2=1
    succ3=1
    while True:
        numero = random.randint(0,36)
        if 1<=numero and numero<=18:
            creditos += apuesta1
            succ1-=2
            if succ1 <= 1:
                succ1 = 1
            apuesta1 = fib(succ1)
        else:
            creditos -= apuesta1
            succ1+=1
            apuesta1 = fib(succ1)
        if numero%2==0 and numero!=0:
            creditos += apuesta2
            succ2-=2
            if succ2 <= 1:
                succ2 = 1
            apuesta2 = fib(succ2)
        else:
            creditos -= apuesta2
            succ2+=1
            apuesta2 = fib(succ2)
        if numero in negros:
            creditos += apuesta3
            succ3-=2
            if succ3 <= 1:
                succ3 = 1
            apuesta3 = fib(succ3)
        else:
            creditos -= apuesta3
            succ3+=1
            apuesta3 = fib(succ3)
        if apuesta1 > 400 or apuesta2 > 400 or apuesta3 > 400 or creditos - apuesta1 - apuesta2 - apuesta3 < 0:
            return 0
        if creditos >= final:
            return 1

def probabilidad(final):
    return sum(partida(1000,final) for x in xrange(2000))/float(2000)

    
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
