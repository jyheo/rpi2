import smbus
import time
import sys

bus = smbus.SMBus(1)

address = 0x48

if len(sys.argv) == 2:
	v = int(sys.argv[1])
	bus.write_byte_data(address, 0x40, v)
else:
	print 'sudo python yl40w.py 0~255'
