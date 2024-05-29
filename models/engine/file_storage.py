#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            return {key:values for key,
                    values in self.__objects.items()
                    if isinstance(values, cls)
                }
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

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
        from os import path
        if path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                serialized_ob = json.load(file)
                for key, obj_value in serialized_ob.items():
                    class_name, obj_id = key.split('.')
                    obj_cname = globals()[class_name]
                    obj_instance = obj_cname(**obj_value)
                    self.__objects[key] = obj_instance

    def delete(self, obj=None):
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