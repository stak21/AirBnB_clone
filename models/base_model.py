#!/usr/bin/python3
""" Class: Base Model """
import uuid
from datetime import datetime
import models


class BaseModel():
    """ A baseclass for future subclasses """
    def __init__(self, *args, **kwargs):
        """ Instantiates the base model variables """
        if kwargs:
            self.__dict__ = kwargs
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ create a string that prints class name, id, dict """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the updated_at variable with the current time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        dic = {key: val for key, val in self.__dict__.items()}
        dic['updated_at'] = str(dic['updated_at'])
        dic['created_at'] = str(dic['created_at'])
        dic['__class__'] = self.__class__.__name__
        
        return dic
