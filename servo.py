import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(5)

for angle in [0, 180]:
  duty = float(angle) / 10.0 + 2.5
  pwm.ChangeDutyCycle(duty)
  time.sleep(1)

for angle in range(1, 185, 30):
  duty = float(angle) / 10.0 + 2.5
  pwm.ChangeDutyCycle(duty)
  time.sleep(1)
