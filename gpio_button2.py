import RPi.GPIO as GPIO
import time

def button_pressed(channel):
	print("Button pressed.")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 21

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

GPIO.add_event_detect(button, GPIO.RISING, bouncetime=200) # rising edge detection 
GPIO.add_event_callback(button, button_pressed) # callback



while True:
	continue	
