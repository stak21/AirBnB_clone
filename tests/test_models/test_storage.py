#!/usr/bin/python3
"""
UnitTest for filestorage: This class manages objects in storage letting you
save, reload, and create
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import os
import json
from pathlib import Path


class TestStorage(unittest.TestCase):
    """ Tests the file storage """
    def setUp(self):
        """ 
            Sets up an instance of storage and refreshes the __object to {}
            reload in our case will create a file with an empty dictionary
        """
        self.storage = FileStorage()
        self.storage._refresh()
        self.storage.reload()

    def tearDown(self):
        """ Removes the file after every test """
        os.remove("./file.json")

    """ Save: Saves the dictionary stored in __object to a file """
    def test_save_empty(self):
        """ Tests if save wrote to the file an empty dictionary """
        self.storage.save()
        with open("file.json", 'r', encoding="utf-8") as f:
            self.r = f.read()
            self.assertEqual(self.r, "{}")

    def test_save_object(self):
        """ Tests if save wrote an object to the file """
        base = BaseModel()
        self.storage.new(base)
        self.storage.save()
        with open("file.json", 'r', encoding="utf-8") as f:
            self.r = f.read()
            self.assertEqual(len(self.r), 212)

    """ new: stores inside of __object a dictionary rep of the given object """
    def test_new(self):
        """ tests if storage was incremented by one object """
        self.base = BaseModel()
        self.storage.new(self.base)
        self.assertEqual(len(self.storage.all()), 1)

    def test_new_if_classes_of_basemodel(self):
        """ Tests new by providing a bad object """ 
        with self.assertRaises(TypeError):
            self.storage.new([])


    """ reload: returns a dictionary stored inside of a file """
    def test_reload(self):
        """ tests if reload properly loads the dictionary object with 2 items"""
        self.test_dictionary = {"BaseModel.121212": {"id": 121212}}
        self.test_dictionary["BaseModel.221212"] = {"id": 121212}
        with open("file.json", 'w+') as f:
            json.dump(self.test_dictionary, f)
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 2)

    def test_reload_no_existing_file(self):
        """ Tests reload with no existing file """
