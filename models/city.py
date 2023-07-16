#!/usr/bin/python3
"""
ALX HolbertonBnB - City

This module defines the City class, which represents a city in the HolbertonBnB application.

Attributes:
    state_id (str): The ID of the state to which the city belongs.
    name (str): The name of the city.

Methods:
    __init__(self, *args, **kwargs): Initializes a new instance of City.

Usage:
    # Creating a new instance
    new_city = City()
    new_city.state_id = "state-123"
    new_city.name = "San Francisco"
    new_city.save()

    # Accessing instance attributes
    print(new_city.state_id)
    print(new_city.name)

    # Converting instance to dictionary
    city_dict = new_city.to_dict()

    # Updating instance and saving changes
    new_city.name = "New York"
    new_city.save()

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    The City class represents a city in the HolbertonBnB application.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
