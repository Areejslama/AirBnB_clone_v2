#!/usr/bin/python3
"""this script to start flask"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def welcome():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_text(text):
    new_text = text.replace("_", " ")
    return f'C {new_text}'


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_massege(text):
    new_text = text.replace("_", " ")
    return f'Python {new_text}'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
