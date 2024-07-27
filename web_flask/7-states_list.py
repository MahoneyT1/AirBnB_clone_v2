#!/usr/bin/python3
"""Flask app """

from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.before_request
def before_request():
    g.db = storage()


@app.teardown_appcontext
def close(exception=None):
    """Closes the storage session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """List all states"""

    states = storage.all()
    return render_template(
            '7-states_list.html',
            states=states
            )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
