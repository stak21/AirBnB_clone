#!/usr/bin/python3
"""importing from BaseModel to build City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """making a City class from BaseModel"""
    state_id = ""
    name = ""
