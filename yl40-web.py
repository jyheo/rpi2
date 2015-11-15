import smbus
import time
import sys
from flask import Flask

app = Flask(__name__)

bus = smbus.SMBus(1)
address = 0x48

@app.route("/ain/<int:ain_addr>")
def analog_in(ain_addr):
	# 192.168.0.6:5000/ain/0
	bus.write_byte(address, 0x40 + ain_addr)
	bus.read_byte(address)
	aread = bus.read_byte(address)
	return 'Ain%d %d' % (ain_addr, aread)

@app.route("/aout/<int:val>")
def analog_out(val):
	# 192.168.0.6:5000/aout/0
	bus.write_byte_data(address, 0x40, val)
	return 'Aout %d' % (val)

if __name__ == "__main__":
	app.run(host="0.0.0.0")

