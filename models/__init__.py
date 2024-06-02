#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from dotenv import load_dotenv
from models.place import Place
from models.city import City
from models.state import State
from models. user import User


load_dotenv()

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

elif os.getenv('HBNB_TYPE_STORAGE') == 'file':
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
