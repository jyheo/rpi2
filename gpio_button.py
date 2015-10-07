import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 21

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

while True:
	if GPIO.input(button) == False:
		print("Button pressed.")
		break

