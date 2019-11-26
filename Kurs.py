#import RPi.GPIO as GPIO
#import tm1637
from wiringpi import wiringPiSetupGpio, pinMode, digitalRead, digitalWrite, GPIO
import RPi.GPIO as IO
#CLK=21
#DIO=20

INP=17
IO.setmode(IO.BCM)
IO.setup(INP,IO.IN)

print(IO.input(INP))

#display = tm1637.TM1637(clk=CLK, dio=DIO)

#from time import sleep
#for i in range(128):
#    display.brightness(7)
#    display.show('sos')
#    sleep(1)
#    display.brightness(0)
#    display.scroll('we dont need sessia')
#    sleep(1)
