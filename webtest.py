from flask import Flask,redirect,url_for,render_template,request,flash
from func import DBserver,Crm,Product

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/form01')
def form01():
    res=Product.colnames()
    return render_template('form01.html',data=res)
@app.route('/search01')
def search01():
    names=Product.colnames()
    return render_template('search01.html',formdata=names)
@app.route('/echarts01')
def echarts01():
    return render_template('echart01.html')
@app.route('/list01')
def list01():
    res=Product.fetchall(10)
    res.insert(0,Product.colnames())
    return render_template('list01.html',data=res)
@app.route('/getform',methods=["get","post"])
def getform():
    a=request.form
    l=Product(**a)
    print(l.info)
    if l.save():
        flash("提交成功")
    else:
        flash("提交失败")
    return redirect(url_for("form01"))
@app.route('/search',methods=["get","post"])
def search():
    a=request.form
    l=Product(**a)
    res=l.search()
    names=l.colnames()
    if res==[]:
        flash('没有查到结果')
    res.insert(0,names)
    return render_template('search01.html',formdata=names, listdata=res)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

