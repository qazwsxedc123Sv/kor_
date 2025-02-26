import RPi.GPIO as G 

G.setwarnings(False)
G.setmode (G.BCM)
G.setup(24, G.OUT)
p = G.PWM(24, 1000)
p.start(0)

try: 
    while True:
        f = int(input())
        p.ChangeDutyCycle(f)
        print((3.3*f)/100) 

finally:
    p.stop()
    G.output (24, 0)
    G.cleanup()
