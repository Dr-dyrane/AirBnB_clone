#!/usr/bin/python3
"""
ALX HolbertonBnB - Review

This module defines the Review class, which represents a review in the HolbertonBnB application.

Attributes:
    place_id (str): The ID of the place associated with the review.
    user_id (str): The ID of the user who wrote the review.
    text (str): The content of the review.

Methods:
    __init__(self, *args, **kwargs): Initializes a new instance of Review.

Usage:
    # Creating a new instance
    new_review = Review()
    new_review.place_id = "place-123"
    new_review.user_id = "user-456"
    new_review.text = "Great place to stay!"
    new_review.save()

    # Accessing instance attributes
    print(new_review.place_id)
    print(new_review.text)

    # Converting instance to dictionary
    review_dict = new_review.to_dict()

    # Updating instance and saving changes
    new_review.text = "Amazing experience!"
    new_review.save()

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    The Review class represents a review in the HolbertonBnB application.

    Attributes:
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
