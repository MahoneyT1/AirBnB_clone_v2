#!/usr/bin/python3
from dotenv import load_dotenv
import os
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError


class DBStorage:
    """
    class DBStorage blueprint/ model
    """
    from models.base_model import BaseModel
    from models.user import User
    from models.place import Place
    from models.state import State
    from models.city import City
    from models.amenity import Amenity
    from models.review import Review

    # private class attributes
    __engine = None
    __session = None

    # object containing key/pair of all the class
    classes = {
    'BaseModel': BaseModel,
    'User': User,
    'Place': Place,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Review': Review
    }

    # initialize HBNB_ENVIROMENT VARIABLE
    def __init__(self):
        # load evn
        load_dotenv()

        con_string = os.getenv("CONN_STRING")

        # create engine
        self.__engine = create_engine(con_string,
                                      echo=True,
                                      pool_pre_ping=True
                                      )
        if os.getenv('HBNB_ENV') == 'test':
            # drop all tables
            Base.metadata.drop_all(self.__engine)
        
        # else create engine schema
        Base.metadata.create_all(self.__engine)
        self.__session_factory = sessionmaker(bind=self.__engine,
                                              expire_on_commit=False)
        self.__session = scoped_session(self.__session_factory)
            
    def all(self, cls=None):
        """
        method that returns list of class present
        if cls is None returns all objects
        else returns all obj in database
        """
        try:
            if cls:
                if cls in self.classes:
                    cls = self.classes[cls]
                    return self.__session.query(cls).all()
            else:
                object = {}
                for class_name, class_type in self.classes.items():
                    object[class_name] = self.__session.query(class_type).all()
                return object
        except SQLAlchemyError as e:
                print(f"Error querring database: {e}")
        
    def new(self, obj):
        """
        add the object to the current database
        session (self.__session)
        """
        try:
            self.__session.add(obj)
        except SQLAlchemyError as e:
            print(f"Error adding object to session: {e}")

    def save(self):
        """
        # commit all changes of the current database
        # session (self.__session)
        """
        try:
            self.__session.commit()
        except SQLAlchemyError as e:
            self.__session.rollback()
            print(f"Error committing session: {e}")

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        try:
            if obj:
                self.__session.delete(obj)
        except SQLAlchemyError as e:
            print(f"deleting object in session error {e}")

    def reload(self):
        """
        create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        self.__session_factory = sessionmaker(self.__session_factory,
                                              expire_on_commit=False)
        self.__session = scoped_session(self.__session_factory)

    def close(self):
        """Close the session."""
        self.__session.remove()
