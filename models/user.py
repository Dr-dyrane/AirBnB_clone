#!/usr/bin/python3
"""
ALX HolbertonBnB - User

This module defines the User class, which represents a user
in the HolbertonBnB application.

Attributes:
    email (str): The email address of the user.
    password (str): The password of the user.
    first_name (str): The first name of the user.
    last_name (str): The last name of the user.

Methods:
    __init__(self, *args, **kwargs): Initializes a new instance of User.

Usage:
    # Creating a new instance
    new_user = User()
    new_user.email = "john@example.com"
    new_user.password = "password"
    new_user.first_name = "John"
    new_user.last_name = "Doe"
    new_user.save()

    # Accessing instance attributes
    print(new_user.email)
    print(new_user.first_name)

    # Converting instance to dictionary
    user_dict = new_user.to_dict()

    # Updating instance and saving changes
    new_user.password = "new_password"
    new_user.save()

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    The User class represents a user in the HolbertonBnB application.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
