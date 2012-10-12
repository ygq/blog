from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash,jsonify

DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

frontend = Flask(__name__)
frontend.config.from_object(__name__)

@frontend.route('/')
def index():
    return render_template('frontend/index.html')

@frontend.route('/reg/')
def reg():
    return render_template('frontend/reg.html')

@frontend.route('/reg_1/')
def reg_1():
    return render_template('frontend/reg_1.html')

@frontend.route('/material/')
def material():
    return render_template("frontend/material.html")

@frontend.route('/login/')
def login():
    return render_template('frontend/login.html')

@frontend.route('/table/')
def table():
    arr = [
           {'name':'baidu.com','shulu':'345','kuaizhao':'2012-10-11','br':'3','pr':'4','prshu':'sdf','alexa':'2334423'},
           {'name':'gogle.com','shulu':'254','kuaizhao':'2012-10-14','br':'8','pr':'5','prshu':'sdf','alexa':'2423'},
           {'name':'soso.com','shulu':'534','kuaizhao':'2012-10-9','br':'4','pr':'5','prshu':'sdf','alexa':'90823'},
           {'name':'sogou.com','shulu':'345','kuaizhao':'2012-10-2','br':'2','pr':'6','prshu':'sdf','alexa':'2363'},
           {'name':'youdao.com','shulu':'3593','kuaizhao':'2012-10-9','br':'2','pr':'3','prshu':'sdf','alexa':'533423'},
           {'name':'yahou.com','shulu':'393','kuaizhao':'2012-10-54','br':'5','pr':'7','prshu':'sdf','alexa':'2523'}
           ]
    return render_template('frontend/table.html',arr=arr)

@frontend.route('/user/')
def user():
    name = request.args.get('name')
    password = request.args.get('password')
    if name != frontend.config['USERNAME']:
        error = 'Invalid password'
    elif password != frontend.config['PASSWORD']:
        error = 'Invalid password'
    else:
        return redirect(url_for('index'))
    #return render_template('frontend/login.html')

if __name__ == "__main__":
    frontend.run()