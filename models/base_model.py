#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import json


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, unique=True,
                nullable=False, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.utcnow()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""

        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    # vars is used to convert class to object
    def to_dict(self):
        """Convert instance into dict format"""

        new_obj = {}
        new_obj = self.__dict__.copy()

        new_obj['__class__'] = self.__class__.__name__
        if 'created_at' in new_obj and isinstance(
            new_obj['created_at'], datetime):
            new_obj['created_at'] = new_obj['created_at'].isoformat()

        if 'updated_at' in new_obj and isinstance(
            new_obj['updated_at'], datetime):
            new_obj['updated_at'] = new_obj['updated_at'].isoformat()

        if '_sa_instance_state' in new_obj.keys():
            del new_obj['_sa_instance_state']
        return new_obj

    def delete(self):
        """
        to delete the current instance from the storage
        (models.storage) by calling the method delete
        """

        from models import storage

        # call the method delete of file-storage
        storage.delete(self)
