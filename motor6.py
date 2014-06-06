import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)

Motor1A = 16
Motor1B = 18
Motor1E = 22

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

pwm = GPIO.PWM(Motor1A, 100)
pwm.start(5)

GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
#GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)

for speed in range(0, 100, 5):
  print "Speed " + str( speed )
  pwm.ChangeDutyCycle(speed)
  time.sleep(5)


GPIO.cleanup()

