import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 50) # 50Hz
pwm.start(1)

if len(sys.argv) != 2:
	print 'sudo python servo.py 1~3'
else:
	ms = float(sys.argv[1])
	dcycle = ms / 20.0 * 100
	pwm.ChangeDutyCycle(dcycle)

time.sleep(2)
