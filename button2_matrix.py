import RPi.GPIO as GPIO
import max7219.led as led
import time

device = led.matrix()
xpos = 0
device.pixel(xpos, 3, 1)

def button_pressed(channel):
	global xpos
	newxpos = xpos + 1
        if newxpos >= 8:
                newxpos = 0
        device.pixel(xpos, 3, 0)
        device.pixel(newxpos, 3, 1)
        xpos = newxpos
	print("Button pressed.")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 21

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

GPIO.add_event_detect(button, GPIO.RISING, bouncetime=200) # rising edge detection 
GPIO.add_event_callback(button, button_pressed) # callback



while True:
	continue	
