from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)


#config.from_object('config')
#from app import views


# @app.route('/')
# def hello_world():
#     return 'Hello, World!!'
#
# @app.route('/login')
# def login():
#     return 'login page!'

import review_app.views #keep at the end to avoid Circular Imports!
