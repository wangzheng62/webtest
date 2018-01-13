from flask import Flask,redirect,url_for,render_template
from alarmclock import alarmclock
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/form01')
def form01():
    return render_template('form01.html')
@app.route('/echarts01')
def echarts01():
    return render_template('echarts01.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
