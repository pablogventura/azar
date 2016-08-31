import random
negros = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
class Valores(object):
    def __init__(self):
        self.papel = [1,2,3,4]
    def proxima_apuesta(self):
        if not self.papel:
            self.papel=[1,2,3,4]
        #print  self.papel[0] + self.papel[-1]
        return self.papel[0] + self.papel[-1]
    def gane(self):
        if self.proxima_apuesta()>= 5000:
            self.papel=[1,2,3,4]
        else:
            self.papel.append(self.proxima_apuesta())
    def perdi(self):
        del self.papel[0]
        if self.papel:
            del self.papel[-1]

def partida(inicial,topemaximo):
    vmayor = Valores()
    vmenor = Valores()
    vpar = Valores()
    vimpar = Valores()
    vrojo = Valores()
    vnegro = Valores()
    creditos=inicial
    while True:
        salio = random.randint(0,36)
        #print sum([ll.proxima_apuesta() for ll in [vmayor,vmenor,vpar,vimpar,vrojo,vnegro]])
        #print creditos
        #print [ll.proxima_apuesta() for ll in [vmayor,vmenor,vpar,vimpar,vrojo,vnegro]]
        if creditos - sum([ll.proxima_apuesta() for ll in [vmayor,vmenor,vpar,vimpar,vrojo,vnegro]]) < 0:
            print "jorge"
            return 0
        if creditos >= topemaximo:
            return 1
        if creditos < 0:
            return 0
        if salio == 0:
            creditos -= vmayor.proxima_apuesta()
            vmayor.perdi()
            creditos -= vmenor.proxima_apuesta()
            vmenor.perdi()
            creditos -= vpar.proxima_apuesta()
            vpar.perdi()
            creditos -= vimpar.proxima_apuesta()
            vimpar.perdi()
            creditos -= vrojo.proxima_apuesta()
            vrojo.perdi()
            creditos -= vnegro.proxima_apuesta()
            vnegro.perdi()
        else:        
            if salio in range(1,19):
                creditos += vmayor.proxima_apuesta() * 2
                creditos -= vmenor.proxima_apuesta()
                vmayor.gane()
                vmenor.perdi()
            else:
                creditos += vmenor.proxima_apuesta() * 2
                creditos -= vmayor.proxima_apuesta()
                vmenor.gane()
                vmayor.perdi()
            if salio in range(2,37,2):
                creditos += vpar.proxima_apuesta() * 2
                creditos -= vimpar.proxima_apuesta()
                vpar.gane()
                vimpar.perdi()
            else:
                creditos += vimpar.proxima_apuesta() * 2
                creditos -= vpar.proxima_apuesta()
                vimpar.gane()
                vpar.perdi()
            if salio in negros:
                creditos += vnegro.proxima_apuesta() * 2
                creditos -= vrojo.proxima_apuesta()
                vnegro.gane()
                vrojo.perdi()
            else:
                creditos += vrojo.proxima_apuesta() * 2
                creditos -= vnegro.proxima_apuesta()
                vrojo.gane()
                vnegro.perdi()

        
def probabilidad(inicial,final):
    return sum(partida(inicial,final) for x in xrange(100))/float(100)

    
import matplotlib.pyplot as plt
import numpy as np
print probabilidad(5000,10000)

