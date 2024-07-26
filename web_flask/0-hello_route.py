#!/usr/bin/python3
"""A script that starts a Flask web application
Your web application must be listening on 0.0.0.0,
port 5000
"""


from flask import Flask, make_response, jsonify
from markupsafe import escape


# An instance of flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def display():
    """Displays (Hello HBNB!)
    """
    return escape("Hello HBNB!")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)