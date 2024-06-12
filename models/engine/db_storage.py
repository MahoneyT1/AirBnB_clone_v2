#!/usr/bin/python3
from dotenv import load_dotenv
import os
from models.base_model import Base, BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError


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
        query on the current database session (self.__session) all objects depending of the class name
        (argument cls)

        if cls=None, query all types of objects (User, State, City, Amenity, Place and Review)
        this method must return a dictionary: (like FileStorage)
        key = <class-name>.<object-id>
        value = object
        """
        new_list = []
        result = None

        if cls:
            for k, v in self.classes.items():
                if k == cls:
                    new_obj = {}
                    class_name = v
                    result = self.__session.query(class_name).all()

                    for dat, v in self.classes.items():
                        key = f"{v.__class__.__name__} ({v.id})"
                        new_obj[key] = v.to_dict()
                        new_list.append(new_obj)
                        
                    return new_obj

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
        self.__session.close()