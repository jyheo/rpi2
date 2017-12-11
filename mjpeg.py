from flask import Flask, render_template, Response, redirect, send_file
from picamera import PiCamera
import io


camera = PiCamera()
camera.resolution = (320, 240)
app = Flask(__name__)


@app.route('/')
def index():
    return  render_template('mjpeg.html', annotate_text="")


@app.route('/config_annotate/<text>')
def config_annotate(text):
    camera.annotate_text = text
    print(text)
    return 'OK'


@app.route('/config_brightness/<int:num>')
def config_brightness(num):
    camera.brightness = num
    return 'OK'


def get_frame():
    stream = io.BytesIO()
    camera.capture(stream, 'jpeg', use_video_port=True)
    stream.seek(0)
    return stream.read()


def gen():
    while True:
        frame = get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/capture')
def capture():
    camera.capture('foo.jpg')
    return send_file('foo.jpg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)

