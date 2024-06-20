#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import os
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        self.storage = storage
        self.reset_storage()

    def tearDown(self):
        """ Remove storage file at end of tests """
        self.reset_storage()
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def reset_storage(self):
        """ Helper method to reset storage """
        del_list = []
        for key in self.storage.all().keys():
            del_list.append(key)
        for key in del_list:
            del self.storage.all()[key]

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(self.storage.all()), 0)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = self.storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        self.storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        self.storage.save()
        self.storage.reload()
        loaded = None
        for obj in self.storage.all().values():
            loaded = obj
        self.assertIsNotNone(loaded)
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            self.storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertIsNone(self.storage.reload())

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(self.storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(self.storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        temp = None
        for key in self.storage.all().keys():
            temp = key
        self.assertIsNotNone(temp)
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(self.storage), FileStorage)

    def test_create_State(self):
        """ tests create State console command """
        from models.state import State
        initial_len_of = len(self.storage.all())
        new_state = State()
        new_state.name = "California"
        new_state.id = "006"
        self.storage.new(new_state)
        self.storage.save()
        all_data = self.storage.all(State)
        self.assertTrue(any(data.id == "006" for data in all_data.values()))

    def test_storage_after_class_creation(self):
        """ Check if class instance is created successfully """
        initial_length = len(self.storage.all())
        new_class = BaseModel()
        new_class.name = "my name"
        new_class.save()
        updated_length = len(self.storage.all())
        self.assertEqual(updated_length, initial_length + 1)


if __name__ == '__main__':
    unittest.main()
