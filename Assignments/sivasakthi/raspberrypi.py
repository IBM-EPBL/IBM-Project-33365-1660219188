import RPi.GPIO as GP
import time
GP.setmode(GP.BOARD)
red=7
yellow=11
green=13
GP.setup(red,GP.OUT)
GP.setup(yellow,GP.OUT)
GP.seyup(green,GP.OUT)
while True:
    GP.output(red,True)
    sleep(3)
    GP.output(red,False)
    
    GP.output(yellow,True)
    sleep(1)
    GP.output(yellow,False)
    
    GP.output(green,True)
    sleep(3)
    GP.output(green,False)
    GP.cleanup()
