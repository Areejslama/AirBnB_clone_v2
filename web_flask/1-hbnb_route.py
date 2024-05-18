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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
