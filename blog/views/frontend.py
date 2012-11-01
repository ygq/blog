#conding = utf-8
from functools import wraps
from flask import request, session, g, redirect, url_for, \
     abort, render_template, flash,jsonify,Blueprint
import urllib2
#from blog import frontend
#frontend = Blueprint('frontend', __name__,)
frontend = Blueprint('frontend', __name__,static_folder='static')
def damy(template=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = request.endpoint.replace('.', '/') + '.html'
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator

@frontend.route('/')
@damy()
def index():
    content = urllib2.urlopen('http://corker.cc').read()
    print content


@frontend.route('/reg/')
@damy()
def reg():
    content = urllib2.urlopen('http://corker.cc').read()
    pass
#    return render_template('frontend/reg.html')

@frontend.route('/reg_1/')
@damy()
def reg_1():
    pass

@frontend.route('/material/')
@damy()
def material():
    pass

@frontend.route('/login/')
@damy()
def login():

    pass

@frontend.route('/confirm/')
@damy()
def confirm():
    pass

@frontend.route('/table/')
@damy()
def table():
    arr = [
           {'name':'baidu.com','shulu':'345','kuaizhao':'2012-10-11','br':'3','pr':'4','prshu':'sdf','alexa':'2334423'},
           {'name':'gogle.com','shulu':'254','kuaizhao':'2012-10-14','br':'8','pr':'5','prshu':'sdf','alexa':'2423'},
           {'name':'soso.com','shulu':'534','kuaizhao':'2012-10-9','br':'4','pr':'5','prshu':'sdf','alexa':'90823'},
           {'name':'sogou.com','shulu':'345','kuaizhao':'2012-10-2','br':'2','pr':'6','prshu':'sdf','alexa':'2363'},
           {'name':'youdao.com','shulu':'3593','kuaizhao':'2012-10-9','br':'2','pr':'3','prshu':'sdf','alexa':'533423'},
           {'name':'yahou.com','shulu':'393','kuaizhao':'2012-10-54','br':'5','pr':'7','prshu':'sdf','alexa':'2523'}
           ]
    return {'arr':arr}

@frontend.route('/user/')
@damy()
def user():
    name = request.args.get('name')
    password = request.args.get('password')
    if name != frontend.config['USERNAME']:
        error = 'Invalid password'
    elif password != frontend.config['PASSWORD']:
        error = 'Invalid password'
    else:
        pass
    #return render_template('frontend/login.html')
