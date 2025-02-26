import RPi.GPIO as G
import time as time

def tbin(num):
    return [(num >> i) & 1 for i in range (7, -1, -1)]

G.setwarnings(False)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
G.setmode(G.BCM)
G.setup(dac, G.OUT)

pr = 5
wait = pr / (255*2)
try: 
    n = 1
    while (n>0):
        n = n - 1
        for num in range (0, 256, 1):
            G.output(dac, tbin(num))
            voltage = (float(num) / 256.0) * 3.3
            print("Output voltage is about ", voltage)
            time.sleep(wait)
        for num in range (255, -1, -1):
            G.output(dac, tbin(num))
            voltage = (float(num) / 256.0) * 3.3
            print("Output voltage is about ", voltage) 
            time.sleep(wait)

finally:
    G.output(dac, 0)
    G.cleanup()
    print ("END\n")