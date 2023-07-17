#!/usr/bin/python3
"""
ALX HolbertonBnB - Unit Tests for State

This module contains unit tests for the State class.

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

import unittest
import datetime
from models.state import State


class TestState(unittest.TestCase):
    """
    Test suite for the State class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.state = State()

    def tearDown(self):
        """
        Clean up after each test case.
        """
        self.state = None

    def test_instance(self):
        """
        Test creating an instance of the State class.
        """
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """
        Test the attributes of the State class.
        """
        self.assertTrue(hasattr(self.state, 'name'))

    def test_attribute_types(self):
        """
        Test the attribute types of the State class.
        """
        self.assertIsInstance(self.state.name, str)

    def test_save(self):
        """
        Test the save() method of the State class.
        """
        old_updated_at = self.state.updated_at
        self.state.save()
        new_updated_at = self.state.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict() method of the State class.
        """
        obj_dict = self.state.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('name', obj_dict)

    def test_str(self):
        """
        Test the __str__() method of the State class.
        """
        obj_str = str(self.state)
        self.assertIsInstance(obj_str, str)
        self.assertIn('[State]', obj_str)
        self.assertIn('id', obj_str)
        self.assertIn('created_at', obj_str)
        self.assertIn('updated_at', obj_str)
        self.assertIn('name', obj_str)


if __name__ == "__main__":
    unittest.main()
