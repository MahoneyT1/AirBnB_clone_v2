#!/usr/bin/python3
"""The file that include all route
"""
from api.v1.views import app_views
from flask import jsonify

# create a custom route
@app_views.route('/status', methods=['GET'])
def status():
    """The status route that confirms
    if the server is okay
    """
    return jsonify({'status':'ok'})

@app_views.route('/stats', methods=['GET'])
def stats():
    """Function to return the count of all class objects
    """
    
    from  models import storage
    from models import user, place, review, state, city, amenity

    # create an object and map the count of each instance in
    # the storage
    stat = {
        'users': storage.count(user.User),
        'places': storage.count(place.Place),
        'reviews': storage.count(review.Review),
        'states': storage.count(state.State),
        'cities': storage.count(city.City),
        'amenities': storage.count(amenity.Amenity)
    }
    return stat
