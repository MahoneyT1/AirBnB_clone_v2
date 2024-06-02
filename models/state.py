#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, storage
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


# call the class engine storage attribute
local_session = storage.__session

# call the class session attribute of Dbs
local_engine = storage.__engine


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states', cascade="all, delete, delete-orphan")

# create the engine
Base.metadata.create_all(local_engine)

# add the schma to the database
storage.new(State)

# commit to database
storage.save()