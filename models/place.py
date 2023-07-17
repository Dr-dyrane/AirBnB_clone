#!/usr/bin/python3
"""
ALX HolbertonBnB - Place

This module defines the Place class, which represents a place in
the HolbertonBnB application.

Attributes:
    name (str): The name of the place.
    user_id (str): The ID of the user who owns the place.
    city_id (str): The ID of the city where the place is located.
    description (str): The description of the place.
    number_bathrooms (int): The number of bathrooms in the place.
    price_by_night (int): The price per night to rent the place.
    number_rooms (int): The number of rooms in the place.
    longitude (float): The longitude coordinate of the place's location.
    latitude (float): The latitude coordinate of the place's location.
    max_guest (int): The maximum number of guests the place can accommodate.
    amenity_ids (list): A list of amenity IDs associated with the place.

Methods:
    __init__(self, *args, **kwargs): Initializes a new instance of Place.

Usage:
    # Creating a new instance
    new_place = Place()
    new_place.city_id = "city-123"
    new_place.user_id = "user-456"
    new_place.name = "Cozy Apartment"
    new_place.description = "Beautiful apartment with stunning views."
    new_place.number_rooms = 2
    new_place.number_bathrooms = 1
    new_place.max_guest = 4
    new_place.price_by_night = 100
    new_place.latitude = 37.7749
    new_place.longitude = -122.4194
    new_place.amenity_ids = ["amenity-1", "amenity-2"]
    new_place.save()

    # Accessing instance attributes
    print(new_place.city_id)
    print(new_place.name)

    # Converting instance to dictionary
    place_dict = new_place.to_dict()

    # Updating instance and saving changes
    new_place.name = "Spacious Loft"
    new_place.save()

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    The Place class represents a place/house in the HolbertonBnB application.

    Attributes:
        name (str): The name of the place.
        user_id (str): The ID of the user who owns the place.
        city_id (str): The ID of the city where the place is located.
        description (str): The description of the place.
        number_bathrooms (int): The number of bathrooms in the place.
        price_by_night (int): The price per night to rent the place.
        number_rooms (int): The number of rooms in the place.
        longitude (float): The longitude coordinate of the place's location.
        latitude (float): The latitude coordinate of the place's location.
        max_guest (int): The maximum number of guests
        the place can accommodate.
        amenity_ids (list): A list of amenity IDs associated with the place.
    """

    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_bathrooms = 0
    price_by_night = 0
    number_rooms = 0
    longitude = 0.0
    latitude = 0.0
    max_guest = 0
    amenity_ids = []
