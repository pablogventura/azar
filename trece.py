import win32api, win32con
import pyscreenshot as ImageGrab
import time
import datetime
import pyttsx

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
        if self.proxima_apuesta()>= 2000:
            self.papel=[1,2,3,4]
        else:
            self.papel.append(self.proxima_apuesta())
    def perdi(self):
        del self.papel[0]
        if self.papel:
            del self.papel[-1]

pmenor = (525, 419)
pmayor = (1056, 576)
ppar = (629, 452)
pimpar = (947, 545)
projo = (729, 479)
pnegro = (836, 514)

tirar = (1241,700)
borrar = (820,700)
color = (164,544)
protando = (347,653)
creditos = 0
imnum = {-651500415: 15, -685688573: 26, -1127077623: 4, 1453040397: 17,
         23484559: 30, 1152247321: 16, 942782619: 29, -1792336609: 27,
         -1681096613: 20, 1860271397: 19, 762713385: 28, -1615752787: 24,
         -1100397771: 13, 491126071: 33, 49448073: 12, -1868886471: 8,
         -1072026911: 22, -742992835: 0, -1299567413: 18, -1708290875: 6,
         1046074055: 14, -1764741833: 34, -1429648051: 1, -1744647725: 31,
         -855667751: 11, 887763855: 2, 864700509: 7, -455817759: 23,
         -371617691: 36, 1449852903: 10, 864136045: 25, 1585306685: 21,
         901856083: 9, 2133739253: 5, 1840417527: 32, -1642809095: 35,
         1314379135: 3}


def numero():
    im=ImageGrab.grab(bbox=(120,471,208,529)) # X1,Y1,X2,Y2
    try:
        result = imnum[hash(tuple(im.histogram()))]
    except KeyError:
        raise ValueError("Numero no reconocido")
    return result

def click(xy):
    x,y=xy
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def colorpixel():
    s = ImageGrab.grab()
    return s.getpixel(color)

def rotapixel():
    s = ImageGrab.grab()
    return s.getpixel(protando)

def apostar(amayor,amenor,apar,aimpar,arojo,anegro):
    time.sleep(0.01)
    click(borrar)
    time.sleep(0.01)
    for i in range(amayor):
        click(pmayor)
        time.sleep(0.01)
    for i in range(amenor):
        click(pmenor)
        time.sleep(0.01)
    for i in range(apar):
        click(ppar)
        time.sleep(0.01)
    for i in range(aimpar):
        click(pimpar)
        time.sleep(0.01)
    for i in range(arojo):
        click(projo)
        time.sleep(0.01)
    for i in range(anegro):
        click(pnegro)
        time.sleep(0.01)
    time.sleep(0.05)
    click(tirar)
    time.sleep(0.2)

def rotando():
    r,g,b = rotapixel()
    if r == 135:
        return True
    elif r == 201:
        return False
    else:
        raise ValueError("Color desconocido al ver si esta rotando")

def esperar_resultado():
    while rotando():
        time.sleep(0.01)


def jugar_y_ver(amayor,amenor,apar,aimpar,arojo,anegro):
    apostar(amayor,amenor,apar,aimpar,arojo,anegro)
    esperar_resultado()
    return numero()

def main():
    jugadas = []
    apuestas = []
    numeros = []
    inicial = int(raw_input("Creditos iniciales: "))
    creditos=inicial
    topemaximo = int(raw_input("Credito final esperado: "))
    time.sleep(5)

    vmayor = Valores()
    vmenor = Valores()
    vpar = Valores()
    vimpar = Valores()
    vrojo = Valores()
    vnegro = Valores()
    
    engine = pyttsx.init()

    
    while True:
        print creditos
        if creditos % 10==0:
            engine.say("%s" % (creditos-inicial))
            engine.runAndWait()
        salio = jugar_y_ver(vmayor.proxima_apuesta(),vmenor.proxima_apuesta(),vpar.proxima_apuesta(),vimpar.proxima_apuesta(),vrojo.proxima_apuesta(),vnegro.proxima_apuesta())
        numeros.append(salio)
        print "Salio el %s" % numeros[-1]
        jugadas.append(salio)
        apuestas.append((vmayor.proxima_apuesta(),vmenor.proxima_apuesta(),vpar.proxima_apuesta(),vimpar.proxima_apuesta(),vrojo.proxima_apuesta(),vnegro.proxima_apuesta()))


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

        if creditos - sum([ll.proxima_apuesta() for ll in [vmayor,vmenor,vpar,vimpar,vrojo,vnegro]]) < 0:
            print "No tengo plata para la apuesta"
            break
        if creditos >= topemaximo:
            print("Llegue a la plata esperada")
            break
        if creditos <= 0:
            print("Me quede sin plata")
            break
        print float(jugadas.count(True))/len(jugadas)
    with open("martingala.txt", "a") as log:
        log.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M") + "\n")
        log.write(str([(apuestas[i],jugadas[i]) for i in range(len(apuestas))])+ "\n")
        log.write(str(numeros)+"\n")
        log.write(str(creditos)+"\n\n")
    time.sleep(30)

if __name__ == "__main__":
    main()
