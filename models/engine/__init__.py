#!/usr/bin/python3
"""
ALX HolbertonBnB - Engine Initialization

This module serves as the initialization module for the engine package. It initializes
the FileStorage instance and provides methods to access the storage.

Attributes:
    storage (FileStorage): The instance of FileStorage for the application.

Usage:
    # Importing the storage instance
    from models.engine import storage

    # Reloading objects from the storage
    storage.reload()

    # Accessing all objects
    all_objects = storage.all()

    # Accessing objects of a specific class
    user_objects = storage.all(User)

    # Adding a new object to storage
    new_user = User()
    storage.new(new_user)

    # Saving objects to the storage
    storage.save()

    # Accessing attributes of a class
    attributes = storage.attributes("User")

Authors:
    - Ukpono Umoren
    - Alexander Udeogaranya
"""

from models.engine.file_storage import FileStorage

# Initialize the FileStorage instance
storage = FileStorage()

# Load objects from the storage
storage.reload()
