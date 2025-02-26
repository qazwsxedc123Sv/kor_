import RPi.GPIO as G


def tbin(num):
    return [(num >> i) & 1 for i in range (7, -1, -1)]

G.setwarnings(False)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
G.setmode(G.BCM)
G.setup(dac, G.OUT)

try: 
    while True:
        num = input("Enter a num from 0 to 255: ")
        try: 
            num = int(num)
            if 0 <= num <=255:
                G.output(dac, tbin(num))
                voltage = (float(num) / 256.0) * 3.3
                print("Output voltage is about ", voltage)
            else: 
                if num < 0:
                    print("Number have to be more then zero")
                elif num > 255:
                    print("Number have to less then 255")
        except Exception:
            if num == "q": break
            print ("Enter a num please")

finally:
    G.output(dac, 0)
    G.cleanup()
    print ("END\n")