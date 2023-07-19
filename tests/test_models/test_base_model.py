#!/usr/bin/python3
"""
ALX HolbertonBnB - Unit Tests for BaseModel

This module contains unit tests for the BaseModel class.

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test suite for the BaseModel class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.base_model = BaseModel()

    def tearDown(self):
        """
        Clean up after each test case.
        """
        self.base_model = None

    def test_instance(self):
        """
        Test creating an instance of the BaseModel class.
        """
        self.assertIsInstance(self.base_model, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of the BaseModel class.
        """
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_attribute_types(self):
        """
        Test the attribute types of the BaseModel class.
        """
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_save(self):
        """
        Test the save() method of the BaseModel class.
        """
        old_updated_at = self.base_model.updated_at
        self.assertEqual(self.base_model.save(), None)  # Modified line
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict() method of the BaseModel class.
        """
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_str(self):
        """
        Test the __str__() method of the BaseModel class.
        """
        obj_str = str(self.base_model)
        self.assertIsInstance(obj_str, str)
        self.assertIn('[BaseModel]', obj_str)
        self.assertIn('id', obj_str)
        self.assertIn('created_at', obj_str)
        self.assertIn('updated_at', obj_str)

    def test_create_with_dict(self):
        """
        Test creating an instance of BaseModel with a dictionary.
        """
        obj_dict = {
            'id': '123',
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-01-01T00:00:00.000000',
            'name': 'John Doe'
        }
        obj = BaseModel(**obj_dict)
        self.assertEqual(obj.id, '123')
        self.assertEqual(obj.created_at, datetime.datetime(2022, 1, 1, 0, 0))
        self.assertEqual(obj.updated_at, datetime.datetime(2022, 1, 1, 0, 0))
        self.assertEqual(obj.name, 'John Doe')


if __name__ == "__main__":
    unittest.main()
