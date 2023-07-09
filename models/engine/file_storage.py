#!/usr/bin/python3
"""
ALX HolbertonBnB - File Storage

This module defines the FileStorage class, which handles the serialization and deserialization
of objects to and from JSON format. It manages the storage of objects in a file-based database.

Attributes:
    __file_path (str): The path to the JSON file where objects are stored.
    __objects (dict): A dictionary containing all loaded objects, with their class name and ID as keys.

Methods:
    all(self, cls=None): Retrieves all objects or objects of a specific class.
    new(self, obj): Adds a new object to the storage.
    save(self): Saves all objects to the JSON file.
    reload(self): Loads objects from the JSON file.
    attributes(self, cls_name): Returns the valid attributes and their types for a given class name.

Usage:
    # Creating a new instance of FileStorage
    storage = FileStorage()

    # Loading objects from the JSON file
    storage.reload()

    # Retrieving all objects
    all_objects = storage.all()

    # Retrieving objects of a specific class
    user_objects = storage.all(User)

    # Adding a new object to storage
    new_user = User()
    storage.new(new_user)

    # Saving objects to the JSON file
    storage.save()

    # Retrieving attributes of a class
    attributes = storage.attributes("User")

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """
    The FileStorage class handles the serialization and deserialization of objects
    to and from JSON format. It manages the storage of objects in a file-based database.

    Attributes:
        __file_path (str): The path to the JSON file where objects are stored.
        __objects (dict): A dictionary containing all loaded objects, with their class name and ID as keys.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Retrieves all objects or objects of a specific class.

        Args:
            cls (class): The class of objects to retrieve. If None, retrieves all objects.

        Returns:
            dict: A dictionary containing the retrieved objects.
        """
        if cls is None:
            return self.__objects
        else:
            cls_objects = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    cls_objects[key] = value
            return cls_objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj (BaseModel): The object to add.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Saves all objects to the JSON file.
        """
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """
        Loads objects from the JSON file.
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                objects_dict = json.load(file)

                for key, value in objects_dict.items():
                    class_name = value.get("__class__")
                    if class_name == "BaseModel":
                        obj_instance = BaseModel(**value)
                    elif class_name == "User":
                        obj_instance = User(**value)
                    elif class_name == "State":
                        obj_instance = State(**value)
                    elif class_name == "City":
                        obj_instance = City(**value)
                    elif class_name == "Review":
                        obj_instance = Review(**value)
                    elif class_name == "Amenity":
                        obj_instance = Amenity(**value)
                    elif class_name == "Place":
                        obj_instance = Place(**value)
                    else:
                        continue

                    self.__objects[key] = obj_instance

    def attributes(self, cls_name):
        """
        Returns the valid attributes and their types for a given class name.

        Args:
            cls_name (str): The name of the class.

        Returns:
            dict: A dictionary containing the attributes and their types.
        """
        attributes = {
            "BaseModel": {
                "id": str,
                "created_at": str,
                "updated_at": str
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            },
            "State": {
                "name": str
            },
            "City": {
                "state_id": str,
                "name": str
            },
            "Amenity": {
                "name": str
            },
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str
            }
        }

        return attributes.get(cls_name, {})
