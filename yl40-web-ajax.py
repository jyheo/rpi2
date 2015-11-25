import smbus
import time
import sys
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

bus = smbus.SMBus(1)
address = 0x48

@app.route("/")
def index():
	return redirect(url_for('static', filename='yl40-ajax.html'))

@app.route("/ain/<int:ain_addr>")
def analog_in(ain_addr):
	# 192.168.0.6:5000/ain/0
	bus.write_byte(address, 0x40 + ain_addr)
	bus.read_byte(address)
	aread = bus.read_byte(address)
	return '%d' % (aread)

@app.route("/aout/<int:val>")
def analog_out(val):
	# 192.168.0.6:5000/aout/0
	bus.write_byte_data(address, 0x40, val)
	return '%d' % (val)

if __name__ == "__main__":
	app.debug=True
	app.run(host="0.0.0.0")

