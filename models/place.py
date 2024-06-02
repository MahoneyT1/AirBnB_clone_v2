#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float


# call the class engine storage attribute
local_session = storage.__session

# call the class session attribute of Dbs
local_engine = storage.__engine


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(120), nullable=False)
    description = Column(String(128), nullable=True)
    number_rooms = Column(Integer(), default=0, nullable=False)
    number_bathrooms = Column(Integer(), default=0, nullable=False)
    max_guest = Column(Integer(), default=0, nullable=False)
    price_by_night = Column(Integer(), default=0, nullable=False)
    latitude = Column(Float(), default=0, nullable=True)
    longitude = Column(Float(), default=0, nullable=True)
    amenity_ids = []

# create the database schema
Base.metadata.create_all(local_engine)

# add the new changes
storage.new(Place)

# commit to database
storage.save()