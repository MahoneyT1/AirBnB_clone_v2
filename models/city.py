#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base, storage
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship



local_engine = storage.__engine
local_session = storage.__session


# print(local_engine)

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(68), ForeignKey('states.id'), nullable=False )
    places = relationship('Place', backref='City', cascade="all, delete-orphan")

# create the local engine
Base.metadata.create_all(local_engine)

# add the current engine to the database
storage.new(City)

# commit to database
storage.save()