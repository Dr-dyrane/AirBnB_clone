#!/usr/bin/python3
"""
ALX HolbertonBnB - Unit Tests for Review

This module contains unit tests for the Review class.

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

import unittest
import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test suite for the Review class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.review = Review()

    def tearDown(self):
        """
        Clean up after each test case.
        """
        self.review = None

    def test_instance(self):
        """
        Test creating an instance of the Review class.
        """
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """
        Test the attributes of the Review class.
        """
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_attribute_types(self):
        """
        Test the attribute types of the Review class.
        """
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_save(self):
        """
        Test the save() method of the Review class.
        """
        old_updated_at = self.review.updated_at
        self.review.save()
        new_updated_at = self.review.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict() method of the Review class.
        """
        obj_dict = self.review.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('place_id', obj_dict)
        self.assertIn('user_id', obj_dict)
        self.assertIn('text', obj_dict)

    def test_str(self):
        """
        Test the __str__() method of the Review class.
        """
        obj_str = str(self.review)
        self.assertIsInstance(obj_str, str)
        self.assertIn('[Review]', obj_str)
        self.assertIn('id', obj_str)
        self.assertIn('created_at', obj_str)
        self.assertIn('updated_at', obj_str)
        self.assertIn('place_id', obj_str)
        self.assertIn('user_id', obj_str)
        self.assertIn('text', obj_str)


if __name__ == "__main__":
    unittest.main()
