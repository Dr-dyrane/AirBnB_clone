#!/usr/bin/python3
"""
ALX HolbertonBnB - Unit Tests for City

This module contains unit tests for the City class.

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

import unittest
import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test suite for the City class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.city = City()

    def tearDown(self):
        """
        Clean up after each test case.
        """
        self.city = None

    def test_instance(self):
        """
        Test creating an instance of the City class.
        """
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        """
        Test the attributes of the City class.
        """
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_attribute_types(self):
        """
        Test the attribute types of the City class.
        """
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_save(self):
        """
        Test the save() method of the City class.
        """
        old_updated_at = self.city.updated_at
        self.city.save()
        new_updated_at = self.city.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict() method of the City class.
        """
        obj_dict = self.city.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('state_id', obj_dict)
        self.assertIn('name', obj_dict)

    def test_str(self):
        """
        Test the __str__() method of the City class.
        """
        obj_str = str(self.city)
        self.assertIsInstance(obj_str, str)
        self.assertIn('[City]', obj_str)
        self.assertIn('id', obj_str)
        self.assertIn('created_at', obj_str)
        self.assertIn('updated_at', obj_str)
        self.assertIn('state_id', obj_str)
        self.assertIn('name', obj_str)


if __name__ == "__main__":
    unittest.main()
