#!/usr/bin/python3
from models.base_model import BaseModel
import json


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
        if isinstance(obj, BaseModel):
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (__file_path)"""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            for key, value in self.__objects.items():
                self.__objects[key] = value.to_dict()
            json.dump(self.__objects, f)

    def reload(self):
        """if file exists, public instance method deserializes the JSON file
        to __objects"""
        try:
            with open(self.__file_path) as f:
                instdict = json.load(f)
            for key, value in instdict.items():
                key = key.split(".")
                self.__objects = eval('{}(**value)'.format(key[0]))
        except FileNotFoundError:
             pass

    @classmethod
    def _refresh(cls):
        """refresh the __object to an empty dict."""
        cls.__object = {}
print('hi')
