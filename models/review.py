#!/usr/bin/python3
""" Review module for the HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """

    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    @property
    def review(self, place_id):
        from models import storage

        data = storage.all(Review)
        my_list = []

        for element in data:
            if element.id == place_id:
                my_list.append(element)
        return my_list