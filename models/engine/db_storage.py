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

        username = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")

        con_string = f"mysql+mysqldb://{username}:{password}@{host}/{database}"

        # create engine
        self.__engine = create_engine(con_string,
                                      echo=True,
                                      pool_pre_ping=True
                                      )
        if os.getenv("HBNB_TYPE_STORAGE") == 'test':
            # drop all tables
            Base.metadata.drop_all(self.__engine)
        
        # else create engine schema
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                              expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def all(self, cls=None):
        """
        method that returns list of class present
        if cls is None returns all objects
        else returns all obj in database
        """
        new_object = {}

        if cls:
            # query cls if cls is not None
            instance_class = self.classes.get(cls)
            result = self.__session.query(instance_class).all()
            print(f"Query result: {result}")

            for obj in result:
                key = f"{cls.__class__.__name__}.{obj.id}"
                new_object[key] = obj
                return new_object
        else:
            for class_name, class_obj in self.classes.items():
                result = self.__session.query(class_obj)
                print(f"Query result: {result}")
                for obj in result:
                    key = f"{class_obj.__name__}.{obj.id}"
                    new_object[key] = obj
                return new_object
    def new(self, obj):
        """
        add the object to the current database
        session (self.__session)
        """
        try:
            Session = self.__session()
            Session.add(obj)
        except SQLAlchemyError as e:
            print(f"Error adding object to Session: {e}")
            Session.rollback()

    def save(self):
        """
        # commit all changes of the current database
        # session (self.__session)
        """
        try:
            self.__session.commit()
        except SQLAlchemyError as e:
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
        session_factory = sessionmaker(bind=self.__engine,
                                              expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close the session."""
        self.__sessionclose()