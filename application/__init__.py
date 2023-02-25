from flask import Flask

app = Flask(__name__)

# routing patterns created in routes.py
from application import routes

