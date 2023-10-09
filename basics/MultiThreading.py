from threading import *
from time import sleep
class Satya(Thread):
    def run(self):
        for k in range(4):
            print("Satya")
            sleep(1)
class Muralidhar(Thread):
    def run(self):
        for k in range(4):
            print("Muralidhar")
            print("\n")
            sleep(1)
m1 = Satya()
m2 = Muralidhar()

m1.start()
sleep(0.3)
m2.start()

m1.join()
m2.join()

print("\n")
print("welcome")
