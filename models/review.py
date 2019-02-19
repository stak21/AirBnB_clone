#!/usr/bin/python3
"""importing from BaseModel to build Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """making a Review class from BaseModel"""

    self.place_id = ""
    self.user_id = ""
    self.text = ""
