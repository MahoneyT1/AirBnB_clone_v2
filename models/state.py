#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        from models import storage
        """
        add a public getter method cities to return the list of City
        objects from storage linked to the current State
        """
        # get storage record
        data_obtained = storage.all()
        for data in data_obtained.items():
           print(data_obtained)


