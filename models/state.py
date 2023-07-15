#!/usr/bin/python3
"""
ALX HolbertonBnB - State

This module defines the State class, which represents a state in the HolbertonBnB application.

Attributes:
    name (str): The name of the state.

Methods:
    __init__(self, *args, **kwargs): Initializes a new instance of State.

Usage:
    # Creating a new instance
    new_state = State()
    new_state.name = "California"
    new_state.save()

    # Accessing instance attributes
    print(new_state.name)

    # Converting instance to dictionary
    state_dict = new_state.to_dict()

    # Updating instance and saving changes
    new_state.name = "New York"
    new_state.save()

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    The State class represents a state in the HolbertonBnB application.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
