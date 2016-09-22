from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

# app.config.from_object(review_app)

# app.config.update(dict(
#     SECRET_KEY='development0key',
# ))


import review_app.views #keep at the end to avoid Circular Imports!
