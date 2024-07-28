#!/usr/bin/python3
"""The state view for States and Cities"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def state_city(state_id=None):
    """Lists all States obj"""

    all_state = storage.all(State)

    if state_id:
        state_id = 'State.' + state_id

    return render_template(
        '9-states.html',
        all_state=all_state,
        state_id=state_id
        )


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
