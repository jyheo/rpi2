# Before running this app, install max7218 driver.
# The driver and HOWTO can be found at https://github.com/rm-hull/max7219 

import max7219.led as led
import time

device = led.matrix()
#device.show_message("Hello world!")

for i in range(8):
	device.pixel(1, i, 1)
	time.sleep(0.5)

for i in range(8):
	device.pixel(1, i, 0)
	time.sleep(0.5)
