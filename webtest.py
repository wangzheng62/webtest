from flask import Flask,redirect,url_for,render_template,request,flash
from alarmclock import alarmclock
import time

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/form01')
def form01():
    return render_template('form01.html')
@app.route('/echarts01')
def echarts01():
    return render_template('echart01.html')
@app.route('/list01')
def list01():
    return render_template('list01.html')
@app.route('/getform',methods=["get","post"])
def getform():
    a=request.form
    if save(a):
        flash("提交成功")
    else:
        flash("提交失败")
    return redirect(url_for("form01"))

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

