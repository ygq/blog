#conding = utf-8
from functools import wraps
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash,jsonify,Blueprint
#from blog import admin

#frontend = Blueprint('frontend', __name__,)
admin = Blueprint('admin', __name__,static_folder='static')
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

@admin.route('/admin/')
@damy()
def index():
    ret = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    return render_template('admin/admin.html')