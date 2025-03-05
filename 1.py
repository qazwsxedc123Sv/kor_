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
    for i in range(256):
        g.output(dac, tbin(i))
        time.sleep(0.005)
        compval = g.input(comp)
        if compval == 1:
            return [i,]
    return 0




try:
    while True:
        r = abc()
        voltage = r[0] / 256 * 3.3
        print("val = {} input = {:.2f}".format(r[0],voltage))

        

finally:
    g.output(dac, 0)
    g.cleanup(dac)