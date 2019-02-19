#!/usr/bin/python3
"""importing from BaseModel to build user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Making a User class inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
