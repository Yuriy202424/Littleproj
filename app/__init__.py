from os import getenv
from flask import Flask


SECRET_KEY = getenv("SECRET_KEY")
app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY


from . import routes