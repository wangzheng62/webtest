from flask import Flask,redirect,url_for,render_template
from alarmclock import alarmclock
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/userhome')
def userhome():
    return render_template('userhome.html')
@app.route('/userhome01')
def userhome01():
    return render_template('userhome01.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
