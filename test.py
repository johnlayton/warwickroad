import RPi.GPIO as gpio
import time

#set up pin 14 as an output
gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)

#Make an LED flash on and off forever
while True: 
    gpio.output(18, gpio.HIGH) 
    time.sleep(1) 
    gpio.output(18, gpio.LOW) 
    time.sleep(0.5)

