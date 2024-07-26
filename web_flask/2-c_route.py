#!/usr/bin/python3
"""A script that starts a Flask web application
Your web application must be listening on 0.0.0.0,
port 5000
"""


from flask import Flask, render_template

# An instance of flask
app = Flask(__name__)

@app.route("/", methods=['GET'],
            strict_slashes=False)

def display():
    """Displays “Hello HBNB! """
    return 'Hello HBNB!'

@app.route("/hbnb", methods=['GET'],
                strict_slashes=False)

def display_two():
    """ / hbnb: display HBNB"""
    return 'HBNB'

@app.route("/c/<text>", methods=['GET'],
                    strict_slashes=False)

def display_third(text):
    """Display C"""
    if text:
        text = text.replace('_', ' ')
        return "<HTML> <head><body> %% {{text}} %% </body></head></HTML>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)