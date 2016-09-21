from flask import current_app, Blueprint, jsonify
api = Blueprint('api', __name__)

@api.route("/")
def index():
     # We can use "current_app" to have access to our "app" object
     return "Hello World!"
