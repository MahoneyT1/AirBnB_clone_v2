#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship

place_amenity = Table("place_amenity", metadata=Base.metadata)
place_id = Column(String(60), ForeignKey('places.id'), primary_key=True)
amenity_id = Column(String(60), ForeignKey('amenities.id'), primary_key=True)


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
    amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)