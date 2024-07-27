#!/usr/bin/python3
"""Flask app """

from models import storage
from flask import Flask, render_template, g, jsonify
from models.state import State
from models.base_model import BaseModel
import json


app = Flask(__name__)


@app.before_request
def before_request():
    """ reloads the storage obj before each
    request is sent
    """
    g.db = storage


@app.teardown_appcontext
def close(exception=None):
    """ closes session after each request"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """List all states"""

    data = g.db.all(State)

    new_list = []
    for k, v in data.items():
        new_list.append(v.to_dict())

    return render_template(
            '7-states_list.html',
            new_list=new_list
            )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
