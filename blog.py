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