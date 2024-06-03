#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models of type"""
        if cls:
            my_list = []
            for cls in self.__objects.copy():
                my_list.append(cls)
            return my_list                

    def new(self, obj):
        """ 
        Add a new public instance method: def delete(self, obj=None): to
        delete obj from __objects if it’s inside - if obj is equal to None,
        the method should not do anything
        Update the prototype of def all(self) to def all(self, cls=None) - that
        returns the list of objects of one type of class. Example below with State
        - it’s an optional filtering
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

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
        def reload(self):
            """Loads storage dictionary from file"""
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
            try:
                with open(FileStorage.__file_path, 'r') as f:
                    temp = json.load(f)
                    for key, val in temp.items():
                        class_name = val['__class__']
                        if class_name in classes:
                            self.__objects[key] = classes[class_name](**val)
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