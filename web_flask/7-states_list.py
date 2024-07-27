#!/usr/bin/python3
"""Flask app """

from models import storage
from flask import Flask, render_template, g, jsonify
from models.state import State
from models.base_model import BaseModel
import json


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """List all states"""

    states = sorted(list(storage.all(State).values()),
                    key=lambda x: x.name)
    return render_template(
            '7-states_list.html',
            states=states
            )


@app.teardown_appcontext
def close(exception=None):
    """ closes session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
