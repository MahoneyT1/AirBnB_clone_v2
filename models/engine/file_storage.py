#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models of type"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        # import and stage classes
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        # create an empty to be returned
        new_list = []

        # open the file using with function for auto file close
        with open(self.__file_path, 'r') as file:
            # extract json file and parse to python object
            data = json.load(file)

            # emply object to store
            new_object = {}
            # iterate through new obj and create a key structure
            for ob, v in new_object.items():
                key = f"[{ob.__class__.__name__}] ({ob.id})"
                # parse newly created obj to file storage
                self.__objects[key] = v
            return self.__objects

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
        # class passed is None return / do nothing
        if obj is None:
            return
        
        key_to_delete = None
        # find the key to delete
        for k, v in self.__objects.items():
            if v == obj:
                key_to_delete = k
        # delete the obj
        del self.__objects[key_to_delete]
        # save the file storage
        self.save()

    def close(self):
        self.reload()