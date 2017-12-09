from flask import Flask,redirect,url_for,render_template
from alarmclock import alarmclock
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/test01')
def test01():
    return 'test01!'
@app.route('/alarm')
def alarm():
    return ("闹钟响了,%s" % (time.time()))
def ss():
    return redirect(url_for('alarm'))


if __name__ == '__main__':
    app.run()
