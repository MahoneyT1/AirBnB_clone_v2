#!/usr/bin/python3
""" Place Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
           nullable=False, primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           nullable=False, primary_key=True)
)


class Place(BaseModel, Base):
    """ A place template that maps class to db schema """

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

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def amenities(self):
            """ returns list of amenities """
            from models import storage

            from models.amenity import Amenity
            clss = {'Amenity': Amenity}
            amenity_list = []

            for obj in storage.all(clss['Amenity']):
                amenity_list.append(obj)
            return amenity_list

        @amenities.setter
        def amenities(self, Amenity_id):
            """ methods that sets attribute of amenities """

            from models.base_model import BaseModel
            from models.user import User
            from models.place import Place
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.review import Review

            classes = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
            }
            if hasattr(Amenity, 'amenity_ids'):
                setattr(Amenity, 'amenity_ids', Amenity_id)

    @property
    def reviews(self):
        """ returns a place review where rv place_id == id """

        from models.review import Review
        from models import storage

        all_record_reviews = storage.all(Review)
        place_reviews = [review for review in all_record_reviews.values()
                         if review.place_id == self.id]
        return place_reviews