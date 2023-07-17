#!/usr/bin/python3
"""
ALX HolbertonBnB - Amenity

This module defines the Amenity class, which represents
an amenity provided by a place/house.

Attributes:
    name (str): The name of the amenity.

Methods:
    None

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    The Amenity class represents an amenity provided by a place/house.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
