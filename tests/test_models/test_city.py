#!/usr/bin/python3
"""Unittest module for the City Class.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    """Test Cases for the City class."""

    def setUp(self):
        """This method set up test."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of City class."""

        au = City()
        self.assertEqual(str(type(au)), "<class 'models.city.City'>")
        self.assertIsInstance(au, City)
        self.assertTrue(issubclass(type(au), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of City class."""
        attributes = storage.attributes()["City"]
        c = City()
        for k, v in attributes.items():
            self.assertTrue(hasattr(c, k))
            self.assertEqual(type(getattr(c, k, None)), v)

if __name__ == "__main__":
    unittest.main()
