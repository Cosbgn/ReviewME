#!revmenv/bin/python
from flask import Flask
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()

app = Flask(__name__)
app.config.from_object('config')

from app import views
