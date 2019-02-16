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
        self.storage = FileStorage()
        self.storage._refresh()
        self.storage.reload()
    def tearDown(self):
        os.remove("./file.json")
    def test_save_empty(self):
        self.storage.save()
        with open("file.json", 'r', encoding="utf-8") as f:
            self.r = f.read()
            self.assertEqual(self.r, "{}")

    def test_new(self):
        self.base = BaseModel()
        self.storage.new(self.base)
        self.assertEqual(len(self.storage.all()), 1)

    def test_reload(self):
        self.test_dictionary = {"BaseModel.121212": {"id": 121212}}
        self.test_dictionary2 = {"BaseModel.221212": {"id": 121212}}
        with open("file.json", 'w+') as f:
            json.dump([self.test_dictionary, self.test_dictionary2], f)
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 2)
