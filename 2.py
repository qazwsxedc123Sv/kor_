import RPi.GPIO as g
import time

g.setwarnings(False)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

g.setmode(g.BCM)
g.setup(dac, g.OUT, initial = 0)
g.setup(troyka, g.OUT, initial = g.HIGH)
g.setup(comp, g.IN)

def tbin (num):
    sig = [(num >> i) & 1 for i in range (7, -1, -1)]
    return sig
def abc ():
    e = 128
    n = 0
    while (e>0):
        n+=e
        g.output(dac, tbin(n))
        time.sleep(0.005)
        compval = g.input(comp)
        if compval == 1:
            n-=e
        e//=2
    return n




try:
    while True:
        r = abc()
        voltage = r / 256 * 3.3
        print(r, f"{voltage:.2} V")

        

finally:
    g.output(dac, 0)
    g.cleanup(dac)