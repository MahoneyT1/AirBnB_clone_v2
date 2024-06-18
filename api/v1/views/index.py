#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify

# create a custom route
@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({'status':'ok'})

@app_views.route('/stats', methods=['GET'])
def stats():
    from  models import storage
    all_data = storage.all()

    # Format the data as JSON
    formatted_data = {}
    for key, obj in all_data.items():
        formatted_data[key] = obj.to_dict()  # Assuming `to_dict` method exists in your models

    return jsonify(formatted_data)