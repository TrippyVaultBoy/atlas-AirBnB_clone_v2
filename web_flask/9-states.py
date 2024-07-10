#!/usr/bin/python3
"""This module starts a web Flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State
import os

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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """displays a number"""
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """displays html page"""
    return (render_template("5-number.html", number=n))


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_even(n):
    """displays a HTML page if n is an int"""
    if (n % 2 == 0):
        parity = "even"
    else:
        parity = "odd"
    return (render_template("6-number_odd_or_even.html",
                            number=n, even_odd=parity))


@app.teardown_appcontext
def teardown(exeption):
    """remove current session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_states():
    """display a list of states"""
    all_states = storage.all(State).values()
    states = sorted(all_states, key=lambda i: i.name)
    return (render_template("7-states_list.html", states=states))


@app.route("/cities_by_states", strict_slashes=False)
def list_cities_by_states():
    """display a list of cities by state"""
    list_states = sorted(storage.all("State").values(), key=lambda i: i.name)
    return (render_template("8-cities_by_states.html", states=list_states))

@app.route("/states", strict_slashes=False)
def list_states2():
    """display list all states"""
    states = storage.all("State").values()
    list_states = sorted(states, key=lambda i: i.name)
    return (render_template("9-states.html", states=list_states))

@app.route("/states/<id>", strict_slashes=False)
def states_and_cities(id):
    """display list of cities linked to state"""
    state = storage.get("State", id)
    if state:
        cities = sorted(state.cities, key=lambda i: i.name)
        return (render_template("9-states.html", state=state, cities=cities))
    return (render_template("9-states.html", not_found=True))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
