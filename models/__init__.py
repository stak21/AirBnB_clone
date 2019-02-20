#!/usr/bin/python3
from models.engine import file_storage
"""creates an unique instance of the application."""

storage = file_storage.FileStorage()
storage.reload()
