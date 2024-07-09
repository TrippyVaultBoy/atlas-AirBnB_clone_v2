#!/usr/bin/python3
"""This module starts a web Flask application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_HBNB():
    """prints Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """prints HBNB"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """displays c"""
    return ("C {}".format(text.replace("_", " ")))


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """displays python"""
    return ("Python {}".format(text.replace("_", " ")))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
