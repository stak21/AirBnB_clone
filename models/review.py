#!/usr/bin/python3
"""importing from BaseModel to build Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """making a Review class from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
