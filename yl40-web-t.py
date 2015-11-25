import smbus
import time
import sys
from flask import Flask, render_template

app = Flask(__name__)

bus = smbus.SMBus(1)
address = 0x48

@app.route("/")
@app.route("/temp")
def analog_in():
	# 192.168.0.6:5000/temp
	bus.write_byte(address, 0x40)
	bus.read_byte(address)
	aread = bus.read_byte(address)
	return render_template('temp.html', temperature=aread)

@app.route("/aout/<int:val>")
def analog_out(val):
	# 192.168.0.6:5000/aout/0
	bus.write_byte_data(address, 0x40, val)
	return 'Aout %d' % (val)

if __name__ == "__main__":
	app.run(host="0.0.0.0")

