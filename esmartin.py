import win32api, win32con
import pyscreenshot as ImageGrab
import time
import datetime

negro = (835,513)
tirar = (1241,700)
borrar = (820,700)
color = (164,544)
protando = (347,653)
pdocena = (603,392)
ptrece = (760,411)
pdnueve = (1062,582)

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

def alnegro(docena,trece,dnueve):
    time.sleep(0.2)
    click(borrar)
    time.sleep(0.2)
    for i in range(docena):
        click(pdocena)
        time.sleep(0.2)
    for i in range(trece):
        click(ptrece)
        time.sleep(0.2)
    for i in range(dnueve):
        click(pdnueve)
        time.sleep(0.2)
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
        time.sleep(0.2)
    
    
def salio_negro():
    r,g,b = colorpixel()
    if r == 255 or r == 57:
        return False
    elif r == 41:
        return True
    else:
        raise ValueError("Salio un color desconocido")

def jugar_y_ver(docena,trece,dnueve):
    alnegro(docena,trece,dnueve)
    esperar_resultado()
    salio = numero()
    if 1 <= salio and salio <= 12:
        #docena paga 3
        return True
    elif salio in [13,14,15]:
        #de a tres paga 12
        return True
    elif 19 <= salio and salio <= 36:
        #paga 2
        return True
    else:
        return False

def main():
    jugadas = []
    apuestas = []
    numeros = []
    creditos = int(raw_input("Creditos iniciales: "))
    topemaximo = int(raw_input("Credito final esperado: "))
    time.sleep(5)
    docena = 4
    trece = 1
    dnueve = 6
    
    while True:
        print creditos
        gane = jugar_y_ver(docena,trece,dnueve)
        numeros.append(numero())
        print "Salio el %s" % numeros[-1]
        jugadas.append(gane)
        if gane:
            docena = 4
            trece = 1
            dnueve = 6
        else:
            docena *= 12
            trece *= 12
            dnueve *= 12
##            if creditos - apuesta <= 0:
##                print "No tengo plata para la apuesta"
##                break
##            if apuesta > 400:
##                raise ValueError("Llegue a la apuesta maxima")
##        if creditos >= topemaximo:
##            print("Llegue a la plata esperada")
##            break
##        if creditos <= 0:
##            print("Me quede sin plata")
##            break
##        print float(jugadas.count(True))/len(jugadas)
##    with open("martingala.txt", "a") as log:
##        log.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M") + "\n")
##        log.write(str([(apuestas[i],jugadas[i]) for i in range(len(apuestas))])+ "\n")
##        log.write(str(numeros)+"\n")
##        log.write(str(creditos)+"\n\n")
##    time.sleep(30)

if __name__ == "__main__":
    main()
