import RPi.GPIO as GPIO
from flask import Flask
from flask import render_template

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led=24 # GPIO channel number
button=21 # GPIO channel number

GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('iot.html')


@app.route('/ledon')
def ledon():
    GPIO.output(led, 1)
    return 'LED ON'


@app.route('/ledoff')
def ledoff():
    GPIO.output(led, 0)
    return 'LED OFF'


@app.route('/button')
def button():
    btn_status = GPIO.input(button)
    return 'Button:' + str(btn_status)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

