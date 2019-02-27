#!/usr/bin/python3
""" Class: FileStorage """
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """class that serializes instances to a JSON file and deserializes JSON
    file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """set __objects the obj with key <obj class name>.id
        & adds the new dictionary to __objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (__file_path)"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """if file exists, public instance method deserializes the JSON file
        to __objects"""
        try:
            with open(self.__file_path) as f:
                objs_dict = json.load(f)
            for key, value in objs_dict.items():
                class_key = key.split(".")
                self.__objects[key] = eval(
                    "{}(**{})".format(class_key[0], value))
        except:
            pass

    @classmethod
    def _refresh(cls):
        """refresh the __object to an empty dict."""
        cls.__objects = {}
        with open("file.json", 'w') as f:
            json.dump(cls.__objects, f)
