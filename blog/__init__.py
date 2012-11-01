#conding = utf-8
from flask import Flask
from blog.views.frontend import frontend
from blog.views.admin import admin
app = Flask(__name__)
app.register_blueprint(frontend)
app.register_blueprint(admin,url_prefix='/admin/')
