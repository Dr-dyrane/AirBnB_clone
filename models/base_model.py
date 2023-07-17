#!/usr/bin/python3
"""
ALX HolbertonBnB - Base Model

This module defines the BaseModel class, which serves as the base model for all
other classes in the HolbertonBnB application. It provides common attributes
and methods that are inherited by other classes.

Attributes:
    id (str): The unique identifier of the instance.
    created_at (datetime): The date and time the instance was created.
    updated_at (datetime): The date and time the instance was last updated.

Methods:
    __init__(self, *args, **kwargs): Initializes a new instance of BaseModel.
    __str__(self): Returns a string representation of the instance.
    save(self): Updates the `updated_at` attribute with the current datetime.
    to_dict(self): Returns a dictionary representation of the instance.

Usage:
    # Creating a new instance
    new_instance = BaseModel()
    new_instance.save()

    # Accessing instance attributes
    print(new_instance.id)
    print(new_instance.created_at)
    print(new_instance.updated_at)

    # Converting instance to dictionary
    instance_dict = new_instance.to_dict()

    # Updating instance and saving changes
    new_instance.name = "John Doe"
    new_instance.save()

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage


class BaseModel:
    """
    The BaseModel class serves as the base model for all other classes
    in the HolbertonBnB application.

    Attributes:
        id (str): The unique identifier of the instance.
        created_at (datetime): The date and time the instance was created.
        updated_at (datetime): The date and time the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            FileStorage().new(self)

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: The string representation of the instance.
        """

        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime.
        """

        self.updated_at = datetime.now()
        FileStorage().save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: A dictionary representation of the instance.
        """

        ua_dict = self.__dict__.copy()
        ua_dict["__class__"] = type(self).__name__
        ua_dict["created_at"] = ua_dict["created_at"].isoformat()
        ua_dict["updated_at"] = ua_dict["updated_at"].isoformat()
        return ua_dict
