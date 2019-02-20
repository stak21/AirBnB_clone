#!/usr/bin/python3
""" Class: Base Model """
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """ A baseclass for future subclasses """
    def __init__(self, *args, **kwargs):
        """ Instantiates the base model variables """
        if len(kwargs) > 0:
            self.__dict__ = kwargs
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ create a string that prints class name, id, dict """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the updated_at variable with the current time """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        self.dic = {key: val for key, val in self.__dict__.items()}
        self.dic['updated_at'] = str(self.dic['updated_at'])
        self.dic['created_at'] = str(self.dic['created_at'])
        self.dic['__class__'] = self.__class__.__name__
        return self.dic
