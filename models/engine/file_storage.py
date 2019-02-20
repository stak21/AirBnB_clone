#!/usr/bin/python3
""" Class: FileStorage """
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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (__file_path)"""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """if file exists, public instance method deserializes the JSON file
        to __objects"""
        try:
            with open(self.__file_path) as f:
                self.__objects = json.load(f)
        except:
            pass

    @classmethod
    def _refresh(cls):
        """refresh the __object to an empty dict."""
        cls.__objects = {}
        with open("file.json", 'w') as f:
            json.dump(cls.__objects, f)
