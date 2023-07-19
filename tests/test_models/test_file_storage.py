#!/usr/bin/python3
"""
This module contains unit tests for the FileStorage class.

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test suite for the FileStorage class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.user = User()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.place = Place()
        self.review = Review()

    def tearDown(self):
        """
        Clean up after each test case.
        """
        self.storage = None
        self.base_model = None
        self.user = None
        self.state = None
        self.city = None
        self.amenity = None
        self.place = None
        self.review = None

    def test_all(self):
        """
        Test the all() method of FileStorage.

        Retrieves all objects or objects of a specific class.
        """
        # Test retrieving all objects
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(len(all_objects), 0)

        # Test retrieving objects of a specific class
        user_objects = self.storage.all(User)
        self.assertIsInstance(user_objects, dict)
        self.assertEqual(len(user_objects), 0)

    def test_new(self):
        """
        Test the new() method of FileStorage.

        Adds a new object to the storage.
        """
        # Test adding a new object to the storage
        key = "{}.{}".format(
            type(self.base_model).__name__, self.base_model.id)
        self.assertNotIn(key, self.storage.all())

        self.storage.new(self.base_model)
        self.assertIn(key, self.storage.all())

    def test_save_reload(self):
        """
        Test the save() and reload() methods of FileStorage.

        Saves all objects to the JSON file and loads objects from the JSON file.
        """
        # Test saving and reloading objects
        self.storage.new(self.base_model)
        self.storage.new(self.user)
        self.storage.new(self.state)
        self.storage.new(self.city)
        self.storage.new(self.amenity)
        self.storage.new(self.place)
        self.storage.new(self.review)

        self.storage.save()
        self.storage.reload()

        self.assertEqual(len(self.storage.all()), 7)

    def test_attributes(self):
        """
        Test the attributes() method of FileStorage.

        Returns the valid attributes and their types for a given class name.
        """
        # Test retrieving attributes for different classes
        base_model_attributes = self.storage.attributes("BaseModel")
        self.assertIsInstance(base_model_attributes, dict)
        self.assertIn("id", base_model_attributes)
        self.assertIn("created_at", base_model_attributes)
        self.assertIn("updated_at", base_model_attributes)

        user_attributes = self.storage.attributes("User")
        self.assertIsInstance(user_attributes, dict)
        self.assertIn("email", user_attributes)
        self.assertIn("password", user_attributes)
        self.assertIn("first_name", user_attributes)
        self.assertIn("last_name", user_attributes)

        state_attributes = self.storage.attributes("State")
        self.assertIsInstance(state_attributes, dict)
        self.assertIn("name", state_attributes)

        city_attributes = self.storage.attributes("City")
        self.assertIsInstance(city_attributes, dict)
        self.assertIn("state_id", city_attributes)
        self.assertIn("name", city_attributes)

        amenity_attributes = self.storage.attributes("Amenity")
        self.assertIsInstance(amenity_attributes, dict)
        self.assertIn("name", amenity_attributes)

        place_attributes = self.storage.attributes("Place")
        self.assertIsInstance(place_attributes, dict)
        self.assertIn("city_id", place_attributes)
        self.assertIn("user_id", place_attributes)
        self.assertIn("name", place_attributes)
        self.assertIn("description", place_attributes)
        self.assertIn("number_rooms", place_attributes)
        self.assertIn("number_bathrooms", place_attributes)
        self.assertIn("max_guest", place_attributes)
        self.assertIn("price_by_night", place_attributes)
        self.assertIn("latitude", place_attributes)
        self.assertIn("longitude", place_attributes)
        self.assertIn("amenity_ids", place_attributes)

        review_attributes = self.storage.attributes("Review")
        self.assertIsInstance(review_attributes, dict)
        self.assertIn("place_id", review_attributes)
        self.assertIn("user_id", review_attributes)
        self.assertIn("text", review_attributes)


if __name__ == "__main__":
    unittest.main()
