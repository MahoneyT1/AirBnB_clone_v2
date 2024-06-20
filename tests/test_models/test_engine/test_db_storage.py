#!/usr/bin/python3
""" Test class for db storage"""
import unittest
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class TestDBStorage(unittest.TestCase):
    """ Test class for database storage
    """
    __session = None
    __engine = None

    # set up tear up
    def setUp(self):
        """ connecting to db of test storage using DBStorage clss"""
        if os.getenv("HBNB_TYPE_STORAGE") == "test":

            username = os.getenv('HBNB_MYSQL_USER')
            password = os.getenv("HBNB_MYSQL_PWD")
            host = os.getenv("HBNB_API_HOST")
            database = os.getenv("HBNB_MYSQL_DB")

            connection_string = f"mysql+mysqldb://{username}:{password}@{host}/{database}"
            self.__engine = create_engine(connection_string, echo=True, pool_pre_ping=True)
            Base.metadata.create_all(self.__engine)
            session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
            self.__session = scoped_session(session_factory)

    def tearDown(self):
        self.__session.close()
    
    def test_create_State(self):
        """ validates if State object was created succesfully"""

        state_object = State()
        state_object.name = "California"

        self.__session.add(state_object)
        self.__session.commit()
        
        storage_data = self.__session.query(State).all()
        self.assertEqual([elem.name for elem in storage_data][0], "California" )

if __name__ == "__main__":
    unittest.main()