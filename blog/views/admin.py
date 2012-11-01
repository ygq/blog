#conding = utf-8
from functools import wraps
from flask import g, request, redirect, url_for,Blueprint,render_template
from flask.ext.principal import RoleNeed, Permission,Principal

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

@admin.route('/')
@damy()
def index():
    ret = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    return Response('Only if you are an admin')