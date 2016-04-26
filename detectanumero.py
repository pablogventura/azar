import pyscreenshot as ImageGrab
import win32api, win32con
import time

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


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def numero():
    im=ImageGrab.grab(bbox=(120,471,208,529)) # X1,Y1,X2,Y2
    try:
        result = imnum[hash(tuple(im.histogram()))]
    except KeyError:
        raise ValueError("Numero no reconocido")
    return result

if __name__ == "__main__":
    while True:
        time.sleep(1)
        print numero()
        click(1246,692)
        time.sleep(0.2)
        click(509,743)

