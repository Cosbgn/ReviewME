from flask import Flask
app = Flask(__name__)


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
