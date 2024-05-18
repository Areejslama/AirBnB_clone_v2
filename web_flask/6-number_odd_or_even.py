#!/usr/bin/python3
"""this script to start flask"""
from flask import render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def templete(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def type(n):
    return  render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
