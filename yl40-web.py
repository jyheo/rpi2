import smbus
import time
import sys
import web

bus = smbus.SMBus(1)
address = 0x48

urls = ('/', 'index')

class index:
	def GET(self):
		# 192.168.0.6:8080/?ain=0&aout=on&aout_val=255
		params = web.input(ain=0, aout="off", aout_val=0)
		print params
		ain = int(params.ain)
		aout = str(params.aout)
		aout_val = int(params.aout_val)

		bus.write_byte(address, 0x40 + ain)
		bus.read_byte(address)
		aread = bus.read_byte(address)

		if aout == "on":
			bus.write_byte_data(address, 0x40, aout_val)
		return aread

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()

