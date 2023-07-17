#!/usr/bin/python3
"""
ALX HolbertonBnB - File Storage

This module defines the FileStorage class, which handles
the serialization and deserialization
of objects to and from JSON format. It manages the storage of objects
in a file-based database.

Attributes:
    __file_path (str): The path to the JSON file where objects are stored.
    __objects (dict): A dictionary containing all loaded objects,
    with their class name and ID as keys.

Methods:
    all(self, cls=None): Retrieves all objects or objects of a specific class.
    new(self, obj): Adds a new object to the storage.
    save(self): Saves all objects to the JSON file.
    reload(self): Loads objects from the JSON file.
    attributes(self, cls_name): Returns the valid attributes and their
    types for a given class name.

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
import datetime
import json
import os


class FileStorage:

    """
    The FileStorage class handles the serialization and
    deserialization of objects
    to and from JSON format. It manages the storage of objects
    in a file-based database.

    Attributes:
        __file_path (str): The path to the JSON file where objects are stored.
        __objects (dict): A dictionary containing all loaded objects,
        with their class name and ID as keys.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Retrieves all objects or objects of a specific class.

        Args:
            cls (class): The class of objects to retrieve.
            If None, retrieves all objects.

        Returns:
            dict: A dictionary containing the retrieved objects.
        """
        if cls is None:
            return self.__objects
        else:
            filtered_objects = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    filtered_objects[key] = value
            return filtered_objects

    def new(self, obj):
        """
        Sets new obj in __objects dictionary.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to JSON file.
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """
        Deserializes JSON file into __objects.
        """
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            self.__objects = obj_dict

    def classes(self):
        """
        Returns a dictionary of valid classes and their references.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def attributes(self, cls_name):
        """
        Returns the valid attributes and their types for a given class name.
        """
        attributes = {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
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
        return attributes[cls_name]


if __name__ == "__main__":
    storage = FileStorage()
    storage.reload()
    objects = storage.all()
    print(objects)
