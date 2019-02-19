#!/usr/bin/python3
"""importing from BaseModel to build State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """making a State class from BaseModel"""
    name = ""
