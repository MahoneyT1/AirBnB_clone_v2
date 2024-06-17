from flask import Blueprint

# call the instance of blueprint with app_views as an arg
app_views = Blueprint('app_views', __name__)
from api.v1.views.index import *