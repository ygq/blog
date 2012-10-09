from flask import Flask,render_template
frontend = Flask(__name__)

@frontend.route('/')
def index():
    return render_template('frontend/index.html')

@frontend.route('/reg/')
def reg():
    return render_template('frontend/reg.html')

@frontend.route('/reg_1/')
def reg_1():
    return render_template('frontend/reg_1.html')

if __name__ == "__main__":
    frontend.run(debug = True)