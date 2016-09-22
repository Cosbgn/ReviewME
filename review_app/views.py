from flask import render_template
from review_app import app

@app.route('/')
def hello_world():
    return 'Hello, World!!'

@app.route('/login')
def login():
    return 'login page!'
