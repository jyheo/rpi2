import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trig=24
echo=23

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

while(1):
	GPIO.output(trig, GPIO.LOW)
	time.sleep(2/1000000.0)
	GPIO.output(trig, GPIO.HIGH)
	time.sleep(20/1000000.0)

	GPIO.output(trig, GPIO.LOW)

	while(GPIO.input(echo) == GPIO.LOW):
		pass

	t0 = time.time()

	while(GPIO.input(echo) == GPIO.HIGH):
		pass

	t1 = time.time() - t0

	print t1 / 58.0 * 1000000

	time.sleep(1)

		
