import RPi.GPIO as g
import time

g.setwarnings(False)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

g.setmode(g.BCM)
g.setup(dac, g.OUT, initial = 0)
g.setup(led, g.OUT, initial = 0)
g.setup(troyka, g.OUT, initial = g.HIGH)
g.setup(comp, g.IN)

def tbin (num):
    sig = [(num >> i) & 1 for i in range (7, -1, -1)]
    return sig

def abc2 ():
    e = 128
    n = 0
    while (e>0):
        n+=e
        g.output(dac, tbin(n))
        time.sleep(0.0005)
        compval = g.input(comp)
        if compval == 1:
            n-=e
        e//=2
    return n

def abc1 ():
    for i in range(256):
        g.output(dac, tbin(i))
        time.sleep(0.0005)
        compval = g.input(comp)
        if compval == 1:
            return i
    return 0




try:
    while True:
        r = abc2()
        voltage = r / 256 * 3.3
        g.output(led, tbin(r))
        time.sleep(0.1)
        print(r, f"{voltage:.2} V")

        

finally:
    g.output(dac, 0)
    g.cleanup(dac)