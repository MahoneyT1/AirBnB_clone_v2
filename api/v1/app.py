#!/usr/bin/python3
from flask import Flask
from flask import Blueprint
import os

host = os.getenv('HBNB_API_HOST')
port = os.getenv('HBNB_API_PORT')

app = Flask(__name__)
from models import storage
from api.v1.views import app_views
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_c():
    storage.close()

if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)