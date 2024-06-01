#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from dotenv import load_dotenv

load_dotenv()

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

elif os.getenv('HBNB_TYPE_STORAGE') == 'file':
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()

# models/__init__.py
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State

# Import all models so they are registered with SQLAlchemy
