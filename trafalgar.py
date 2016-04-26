import win32api, win32con
import pyscreenshot as ImageGrab
import time
import datetime
import pyttsx



negro = (835,513)
ppar = (628,444)
pprimeros=(523,418)
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
def makro(n):
    result = 1
    for i in range(n):
        result = result * 2 + 1
    return result

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

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

def alnegro(nn,pp,rr):
    time.sleep(0.01)
    click(borrar)
    time.sleep(0.01)
    for i in range(nn):
        click(negro)
        time.sleep(0.01)
    for i in range(pp):
        click(negro)
        time.sleep(0.01)
    for i in range(rr):
        click(negro)
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
    
    
def salio_negro():
    r,g,b = colorpixel()
    if r == 255 or r == 57:
        return False
    elif r == 41:
        return True
    else:
        raise ValueError("Salio un color desconocido")

def jugar_y_ver(nn,pp,rr):
    alnegro(nn,pp,rr)
    esperar_resultado()
    return salio_negro()

def main():
    succn = 1
    succp = 1
    succr = 1
    jugadas = []
    apuestas = []
    numeros = []
    inicial = int(raw_input("Creditos iniciales: "))
    creditos=inicial
    topemaximo = int(raw_input("Credito final esperado: "))
    time.sleep(5)
    apuestan = fib(succn)
    apuestap = fib(succp)
    apuestar = fib(succr)
    engine = pyttsx.init()

    
    while True:
        print creditos
        if creditos % 10==0:
            engine.say("%s" % (creditos-inicial))
            engine.runAndWait()
        gane = jugar_y_ver(apuestan,apuestap,apuestar)
        numeros.append(numero())
        print "Salio el %s" % numeros[-1]
        jugadas.append(gane)
        apuestas.append(apuesta)
        if gane:
            creditos += apuestan
            succn -= 2
            if succn <= 0:
                succn = 1
            apuestan = fib(succn)
        else:
            creditos -= apuestan
            succn += 1
            apuestan = fib(succn)
            if creditos - apuestan <= 0:
                print "No tengo plata para la apuesta"
                break
            if apuestan > 400:
                raise ValueError("Llegue a la apuesta maxima")
        if numero()%2==0 and numero()!=0:
            creditos += apuestap
            succp -= 2
            if succp <= 0:
                succp = 1
            apuestap = fib(succp)
        else:
            creditos -= apuestap
            succp += 1
            apuestap = fib(succp)
            if creditos - apuestap <= 0:
                print "No tengo plata para la apuesta"
                break
            if apuestap > 400:
                raise ValueError("Llegue a la apuesta maxima")
        if 1<=numero() and numero()<=18:
            creditos += apuestar
            succr -= 2
            if succr <= 0:
                succr = 1
            apuestar = fib(succr)
        else:
            creditos -= apuestar
            succr += 1
            apuestar = fib(succr)
            if creditos - apuestar <= 0:
                print "No tengo plata para la apuesta"
                break
            if apuestar > 400:
                raise ValueError("Llegue a la apuesta maxima")
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
