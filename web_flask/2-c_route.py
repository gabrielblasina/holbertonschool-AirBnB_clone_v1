#!/usr/bin/python3

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    with_space = text.replace('_', ' ')
    return f'C {escape(with_space)}'


if __name__ == '__main__':
    app.run()
