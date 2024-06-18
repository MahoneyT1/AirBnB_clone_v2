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
        method that returns list of class present
        if cls is None returns all objects
        else returns all obj in database
        """
        
        new_dict = {}
        for clss in self.classes:
            if cls is None or cls is self.classes[clss] or cls is clss:
                objs = self.__session.query(self.classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)
       

    def new(self, obj):
        """
        add the object to the current database
        session (self.__session)
        """

        try:
            self.__session.add(obj)
        except SQLAlchemyError as e:
            print(f"Error adding object to Session: {e}")
            self.__session.rollback()

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

    def get(self, cls, id):
        """
        cls: class
        id: string representing the object ID
        Returns the object based on the class and its ID, or None if not found
        """

        my_ob = {}
        my_list = []
        if cls and id:
            for k, v in self.classes.items():
                if v == cls:
                    all_class = self.classes[k]
                    result = self.__session.query(all_class)

                    for b in result:
                        key = f"[{b.__class__.__name__}] ({b.id})"
                        my_ob[key] = vars(b)
                    return my_ob
        return None

    def count(self, cls=None):
        """
        cls: class (optional)
        Returns the number of objects in storage matching the given class.
        If no
        class is passed, returns the count of all objects in storage.
        """

        from sqlalchemy import func
        count_result = 0

        session = self.__session  # Assuming self has a session attribute

        # Count objects of a specific class (if provided)
        if hasattr(self, 'cls') and self.cls:
            return session.query(self.cls).count()

        # Count all objects (using a dummy column for count())
        return session.query(func.count()).count()

    def close(self):
        """Close the session."""
        return self.__session.close()
