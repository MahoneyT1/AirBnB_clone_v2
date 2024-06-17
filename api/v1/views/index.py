#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify

# create a custom route
@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({'status':'ok'})