#!/usr/bin/python3
""" Class: Base Model """
""" Class: Base Model """
from datetime import datetime
from datetime import timedelta
from models import storage
import uuid


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

    def __str__(self):
        """ create a string that prints class name, id, dict """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the updated_at variable with the current time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        return {
                "id": self.id,
                "__class__": self.__class__.__name__,
                "updated_at": self.updated_at.isoformat(),
                "created_at": self.created_at.isoformat()
                }
