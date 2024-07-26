#!/usr/bin/python3
"""Runs a app at 5000 on localhost """

from flask import Flask, render_template, make_response, jsonify
from markupsafe import escape


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


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Display n is a number only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_template(n):
    """renders a template if n is a number"""

    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_template_six(n):
    """ Display even or odd according to the args parsed
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
