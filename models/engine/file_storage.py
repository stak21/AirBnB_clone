#!/usr/bin/python3
import json


class FileStorage():
    """class that serializes instances to a JSON file and deserializes JSON
    file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """set __objects the obj with key <obj class name>.id
        & adds the new dictionary to __objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (__file_path)"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """if file exists, public instance method deserializes the JSON file
        to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                FileStorage.__objects = json.load(f)
        except:
            pass

    @classmethod
    def _refresh(cls):
        """refresh the __object to an empty dict."""
        FileStorage.__object = {}
        with open("file.json", 'w') as f:
            json.dump(FileStorage.__object, f)
