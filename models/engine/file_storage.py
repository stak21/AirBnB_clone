#!/usr/bin/python3
import models
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
        """***sets in __objects the obj with key <obj class name>.id
        adds the new dictionary to __objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = to_dict(obj)

    def save(self):
        """serializes __objects to the JSON file (__file_path)"""
        with open(__file_path, 'w') as f:
            dump(self.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if __file_path:
