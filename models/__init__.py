#!/usr/bin/python3
from models.engine.file_storage import FileStorage
"""creates an unique instance of the application."""


storage = FileStorage()
storage.reload()
