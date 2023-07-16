"""
ALX HolbertonBnB - Storage Module

This module provides a high-level interface for managing the storage system.
It delegates the actual storage operations to the FileStorage class in the models.engine.file_storage module.

Attributes:
    __engine (FileStorage): The storage engine instance.

Methods:
    all(cls=None): Retrieves all objects or objects of a specific class.
    new(obj): Adds a new object to the storage.
    save(): Saves all objects to the storage.
    reload(): Loads objects from the storage.

Usage:
    # Initializing the storage engine
    storage = Storage()

    # Retrieving all objects
    all_objects = storage.all()

    # Retrieving objects of a specific class
    user_objects = storage.all(User)

    # Adding a new object
    new_user = User()
    storage.new(new_user)

    # Saving objects
    storage.save()

    # Reloading objects
    storage.reload()

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

from models.engine.file_storage import FileStorage


class Storage:
    """
    The Storage class provides a high-level interface for managing the storage system.
    It delegates the actual storage operations to the FileStorage class.
    """

    __engine = FileStorage()

    def all(self, cls=None):
        """
        Retrieves all objects or objects of a specific class.

        Args:
            cls (class): The class of objects to retrieve. If None, retrieves all objects.

        Returns:
            dict: A dictionary containing the retrieved objects.
        """
        if cls is None:
            return self.__engine.all()
        else:
            return self.__engine.all(cls)

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj (BaseModel): The object to add.
        """
        self.__engine.new(obj)

    def save(self):
        """
        Saves all objects to the storage.
        """
        self.__engine.save()

    def reload(self):
        """
        Loads objects from the storage.
        """
        self.__engine.reload()
