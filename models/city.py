#!/usr/bin/python3
""" City Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'),
                      nullable=False)
    places = relationship('Place', backref='cities',
                          cascade="all, delete-orphan")

    def cities(self, state_id):
        """
        for FileStorage: getter attribute cities that returns the list
        of City instances with state_id equals to the current State.id =>
        It will be the FileStorage relationship
        between State and City
        """
        from models import storage

        # create an empty list
        list_of_city = []
        data = storage.all(City)

        # loop through all the instances on City
        for cls in data:
            if cls.id == state_id:  # if class.id == State_id passed as var
                list_of_city.append(cls)  # append instance
        return list_of_city
