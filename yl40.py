import smbus
import time
import sys

bus = smbus.SMBus(1)

address = 0x48

# AIN0 0x40: photocell
# AIN1 0x41: thermister
# AIN3 0x43: registance

if len(sys.argv) == 2:
	i = int(sys.argv[1])
	input_addr = 0x40 + i
else:
	input_addr = 0x40 

while True:
	bus.write_byte(address, input_addr)
	bus.read_byte(address)
	aread = bus.read_byte(address)
	print aread
	time.sleep(0.2)

