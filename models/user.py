#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base, storage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship



# call the class engine storage attribute
local_session = storage.__session

# call the class session attribute of Dbs
local_engine = storage.__engine

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship('Place', backref='places', cascade="all, delete-orphan")

# create the engine schema
Base.metadata.create_all(User)

# add the new tables to the db
storage.new(User)

# save the new table to the database
storage.save()