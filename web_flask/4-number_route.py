#!/usr/bin/python3
"""A script that starts a Flask web application
Your web application must be listening on 0.0.0.0,
port 5000
"""
from flask import Flask, render_template, make_response, jsonify

# An instance of flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display():
    """Displays “Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_two():
    """ / hbnb: display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_third(text):
    """Display C"""
    if text:
        text = text.replace('_', ' ')
        return f'C {text}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    """Display 'Python ', followed by the value of
    the text variable (replace underscores with spaces).
    Default value is 'is cool'
    """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<n>', strict_slashes=False)
def display_number(n):
    """Display n is a number only if n is an integer"""

    if n.isdigit() == True:
        return f'{n} is number'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
