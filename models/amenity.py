#!/usr/bin/python3
"""importing from BaseModel to build Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """making an Amenity class from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
