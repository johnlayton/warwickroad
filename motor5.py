import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
# GPIO.setup(18, GPIO.OUT)
# pwm = GPIO.PWM(18, 100)
# pwm.start(5)

# for angle in [0, 180]:
#   duty = float(angle) / 10.0 + 2.5
#   pwm.ChangeDutyCycle(duty)
#   time.sleep(1)

# for angle in range(1, 185, 30):
#   duty = float(angle) / 10.0 + 2.5
#   pwm.ChangeDutyCycle(duty)
#   time.sleep(1)

# import RPi.GPIO as GPIO
# from time import sleep

# GPIO.setmode(GPIO.BOARD)

Motor1A = 16
Motor1B = 18
Motor1E = 22

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

pwm = GPIO.PWM(Motor1B, 100)
pwm.start(5)

for speed in [0, 100]:
  # duty = float(angle) / 10.0 + 2.5
  pwm.ChangeDutyCycle(speed)
  time.sleep(1)

# print "Turning motor on"
# GPIO.output(Motor1A,GPIO.HIGH)
# GPIO.output(Motor1B,GPIO.LOW)
# GPIO.output(Motor1E,GPIO.HIGH)

# sleep(2)

# print "Stopping motor"
# GPIO.output(Motor1E,GPIO.LOW)

GPIO.cleanup()

