#!/usr/bin/python3
"""App Flask """

from flask import Flask, render_template
from models.city import City
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def city_by_state():
    """List Cities by State"""

    states = storage.all(State).values()

    return render_template(
        '8-cities_by_states.html',
        states=states
    )


@app.teardown_appcontext
def close(exception):
    """closes connecton session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
