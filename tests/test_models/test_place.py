#!/usr/bin/python3
"""
ALX HolbertonBnB - Unit Tests for Place

This module contains unit tests for the Place class.

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

import unittest
import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test suite for the Place class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.place = Place()

    def tearDown(self):
        """
        Clean up after each test case.
        """
        self.place = None

    def test_instance(self):
        """
        Test creating an instance of the Place class.
        """
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        """
        Test the attributes of the Place class.
        """
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_attribute_types(self):
        """
        Test the attribute types of the Place class.
        """
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_save(self):
        """
        Test the save() method of the Place class.
        """
        old_updated_at = self.place.updated_at
        self.place.save()
        new_updated_at = self.place.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict() method of the Place class.
        """
        obj_dict = self.place.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('name', obj_dict)
        self.assertIn('user_id', obj_dict)
        self.assertIn('city_id', obj_dict)
        self.assertIn('description', obj_dict)
        self.assertIn('number_bathrooms', obj_dict)
        self.assertIn('price_by_night', obj_dict)
        self.assertIn('number_rooms', obj_dict)
        self.assertIn('longitude', obj_dict)
        self.assertIn('latitude', obj_dict)
        self.assertIn('max_guest', obj_dict)
        self.assertIn('amenity_ids', obj_dict)

    def test_str(self):
        """
        Test the __str__() method of the Place class.
        """
        obj_str = str(self.place)
        self.assertIsInstance(obj_str, str)
        self.assertIn('[Place]', obj_str)
        self.assertIn('id', obj_str)
        self.assertIn('created_at', obj_str)
        self.assertIn('updated_at', obj_str)
        self.assertIn('name', obj_str)
        self.assertIn('user_id', obj_str)
        self.assertIn('city_id', obj_str)
        self.assertIn('description', obj_str)
        self.assertIn('number_bathrooms', obj_str)
        self.assertIn('price_by_night', obj_str)
        self.assertIn('number_rooms', obj_str)
        self.assertIn('longitude', obj_str)
        self.assertIn('latitude', obj_str)
        self.assertIn('max_guest', obj_str)
        self.assertIn('amenity_ids', obj_str)


if __name__ == "__main__":
    unittest.main()
