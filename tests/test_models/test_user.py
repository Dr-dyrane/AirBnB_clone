#!/usr/bin/python3
"""
ALX HolbertonBnB - Unit Tests for User

This module contains unit tests for the User class.

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

import unittest
import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test suite for the User class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.user = User()

    def tearDown(self):
        """
        Clean up after each test case.
        """
        self.user = None

    def test_instance(self):
        """
        Test creating an instance of the User class.
        """
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """
        Test the attributes of the User class.
        """
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_attribute_types(self):
        """
        Test the attribute types of the User class.
        """
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_save(self):
        """
        Test the save() method of the User class.
        """
        old_updated_at = self.user.updated_at
        self.user.save()
        new_updated_at = self.user.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict() method of the User class.
        """
        obj_dict = self.user.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('email', obj_dict)
        self.assertIn('password', obj_dict)
        self.assertIn('first_name', obj_dict)
        self.assertIn('last_name', obj_dict)

    def test_str(self):
        """
        Test the __str__() method of the User class.
        """
        obj_str = str(self.user)
        self.assertIsInstance(obj_str, str)
        self.assertIn('[User]', obj_str)
        self.assertIn('id', obj_str)
        self.assertIn('created_at', obj_str)
        self.assertIn('updated_at', obj_str)
        self.assertIn('email', obj_str)
        self.assertIn('password', obj_str)
        self.assertIn('first_name', obj_str)
        self.assertIn('last_name', obj_str)


if __name__ == "__main__":
    unittest.main()
