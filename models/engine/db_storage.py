#!/usr/bin/python3

from dotenv import load_dotenv
import os
from models.base_model import Base, BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError
from models import base_model, amenity, city, place, review, state, user


class DBStorage:
    """
    class DBStorage blueprint/ model
    """

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

    CNC = {
        'Amenity': amenity.Amenity,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'User': user.User
        }

    # initialize HBNB_ENVIROMENT VARIABLE
    def __init__(self):
        # load evn
        load_dotenv()

        username = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")

        con_string = "mysql+mysqldb://{}:{}@{}/{}".format(username,
                                                          password,
                                                          host,
                                                          database)

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

        obj_dict = {}
        if cls:
            query_data = self.__session.query(cls).all()
            for obj in query_data:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                obj_dict[key] = obj
            return obj_dict
        else:
            for cls in self.classes.values():
                query_data = self.__session.query(cls).all()
                for obj in query_data:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    obj_dict[key] = obj.to_dict()
            return  obj_dict

    def new(self, obj):
        """
        add the object to the current database
        session (self.__session)
        """

        try:
            self.__session.add(obj)
        except SQLAlchemyError as e:
            print("Error adding object to Session: {}".format(e))
            self.__session.rollback()

    def save(self):
        """
        # commit all changes of the current database
        # session (self.__session)
        """

        try:
            self.__session.commit()
        except SQLAlchemyError as e:
            print("Error committing session: {}".format(e))

    def delete(self, obj):
        """
        delete from the current database session obj if not None
        """

        try:
            if obj:
                self.__session.delete(obj)
        except SQLAlchemyError as e:
            print("deleting object in session error {}".format(e))

    def reload(self):
        """
        create all tables in the database
        """

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def get(self, cls, id):
        """
        Retrieves an object from storage based on its class
        and ID.
        Args:
            cls (class): The class of the object to be retrieved.
            id (str): The unique identifier of the object to be
            retrieved.

        Returns:
            object: The object if it exists in storage, or None if
            it does not exist.

        Example:
            Suppose you have an object of class `State` with ID `1234`
            stored in the
            `__objects` dictionary, and you want to retrieve it:

            state = storage.get(State, "1234")

            If the object exists, `state` will be the `State` object
            with ID `1234`.
            If it does not exist, `state` will be None.
        """
        query_result = self.__session.query(cls).get(id)
        return query_result

    def count(self, cls=None):
        """
        Counts the number of objects in storage.
        Args:
            cls (class, optional): The class of objects to
            count. If None, counts all objects.
        Returns:
            int: The number of objects in storage matching the
            given class, or the total
                number of objects if no class is specified.
        Example:
            # Count all objects in storage
            total_objects = storage.count()

            # Count only objects of class 'State'
            state_objects = storage.count(State)
            is passed, returns the count of all objects in storage.
        """
        if cls:
            return len(self.all(cls))
        else:
            return len(self.all())

    def close(self):
        """Close the session."""
        return self.__session.close()
