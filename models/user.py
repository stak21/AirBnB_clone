#!/usr/bin/python3
"""importing from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """user class inherits from BaseModel"""

    def __init__(self, email, password, first_name, last_name):
        """defining public instance attributes"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
