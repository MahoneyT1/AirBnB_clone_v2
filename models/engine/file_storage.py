#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
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

    __file_path = 'file.json'
    __objects = {}

    @classmethod
    def from_json(cls, dict_t):
        """ cls method that returns an instance of cls"""
        return cls(**dict_t)

    def all(self, cls=None):
        """Returns a dictionary of models of type"""

        # an empty dict to collect generated data
        new_ob = {}

        # check if cls is none if not extract the classname
        if cls is not None:
            # class name to print
            cls_to_print = cls

            # loop through reloaded objects in filestorage
            for k, v in self.__objects.items():
                # if v is an instance of class to print
                if isinstance(v, cls_to_print):
                    new_ob[k] = v  # extract k:v
            return new_ob  # return new_object

        # if cls is None loop and extract data
        for k, v in self.__objects.items():
            new_ob[k] = v
        return new_ob  # return new generated object

    def new(self, obj):
        """
        Add a new public instance method: def delete
        (self, obj=None): to delete obj from __objects
        if it’s inside - if obj is equal
        to None, the method should not do anything

        Update the prototype of def all(self) to def all
        (self, cls=None-that returns the list of objects
        of one type of class. Example
        below with State - its an optional filtering
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        me = FileStorage.classes

    def save(self):
        """Saves storage dictionary to file"""

        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        Only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file does not exist, no exception should be raised.
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    class_name = val['__class__']
                    if class_name in self.classes:
                        self.__objects[key] = self.classes[class_name](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Delete method that deletes an object from filestorage
        args:
            args:obj = None which takes an object
        sucess:
            deletes object from filestorage
        """

        if obj is None:
            return
        else:
            # delete obj from __objects if it’s inside
            obj_key = None
            for key, val in self.__objects.items():
                if val == obj:
                    obj_key = key
                    break

            if obj_key is not None:
                del self.__objects[obj_key]

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

        if cls and id:
            key = "{}.{}".format(cls.__name__, id)
            return self.__objects.get(key, None)
        return None

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
        """
        if not cls and id:
            return len(self.all(cls))
        else:
            return len(self.all(cls).keys())
