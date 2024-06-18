#!/usr/bin/python3
"""
Flask route that returns json status response
"""

from api.v1.views import app_views
from flask import jsonify, request

# create a custom route


@app_views.route('/status', methods=['GET'])
def status():
    """The status route that confirms
    if the server is okay
    """
    return jsonify({'status': 'ok'})


@app_views.route('/stats', methods=['GET'])
def stats():
    """Function to return the count of all class objects
    """

    from models import storage
    from models import user, place, review, state, city, amenity

    # create an object and map the count of each instance in
    # the storage

    if request.method == 'GET':
        response = {}

        stat = {
        'users': "User",
        'places': "Place",
        'reviews': "Review",
        'states': "State",
        'cities': "City",
        'amenities': "Amenity"
        }

        for key, value in stat.items():
            response[key] = storage.count(value)
        return jsonify(response)
