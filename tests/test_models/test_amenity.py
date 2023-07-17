#!/usr/bin/python3
"""
ALX HolbertonBnB - Unit Tests for Amenity

This module contains unit tests for the Amenity class.

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

import unittest
import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test suite for the Amenity class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.amenity = Amenity()

    def tearDown(self):
        """
        Clean up after each test case.
        """
        self.amenity = None

    def test_instance(self):
        """
        Test creating an instance of the Amenity class.
        """
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        """
        Test the attributes of the Amenity class.
        """
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_attribute_types(self):
        """
        Test the attribute types of the Amenity class.
        """
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime.datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime.datetime)
        self.assertIsInstance(self.amenity.name, str)


if __name__ == "__main__":
    unittest.main()
