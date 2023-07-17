#!/usr/bin/python3
"""
Unit tests for console.py

This module contains unit tests for the HBNBCommand class in console.py.
The HBNBCommand class represents the command-line interpreter for
the HolbertonBnB application.

Usage:
    $ python3 -m unittest discover tests

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

import unittest
import json
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    Test cases for the HBNB console.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.console = HBNBCommand()

    def tearDown(self):
        """
        Clean up after each test case.
        """
        pass

    def test_quit(self):
        """
        Test quit command.
        """
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_help(self):
        """
        Test help command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = f.getvalue().strip()
            self.assertIn("Documented commands (type help <topic>):", output)
            self.assertIn(
                "EOF  all  count  create  destroy  help  quit  show  update",
                output)

    def test_create(self):
        """
        Test create command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertRegex(
                output, r'^[a-f0-9]{8}-([a-f0-9]{4}-){3}[a-f0-9]{12}$')

    def test_show(self):
        """
        Test show command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertIn(obj_id, output)

    def test_destroy(self):
        """
        Test destroy command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertEqual(output, '')

    def test_all(self):
        """
        Test all command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("create State")
            self.console.onecmd("all")
            output = f.getvalue().strip()
            self.assertIn("BaseModel", output)
            self.assertIn("User", output)
            self.assertIn("State", output)

    def test_update(self):
        """
        Test update command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"update BaseModel {obj_id} name 'new_name'")
            self.console.onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertIn("new_name", output)

    def test_count(self):
        """
        Test count command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("count BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "2")

    def test_invalid_command(self):
        """
        Test invalid command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("invalid_command")
            output = f.getvalue().strip()
            self.assertEqual(output, "*** Unknown syntax: invalid_command")

    def test_invalid_number_of_arguments(self):
        """
        Test invalid number of arguments.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            output = f.getvalue().strip()
            self.assertEqual(output, "** invalid number of arguments **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            output = f.getvalue().strip()
            self.assertEqual(output, "** invalid number of arguments **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all invalid_class")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 12345")
            output = f.getvalue().strip()
            self.assertEqual(output, "** invalid number of arguments **")

    def test_invalid_json_syntax(self):
        """
        Test invalid JSON syntax.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 12345 {invalid_json}")
            output = f.getvalue().strip()
            self.assertEqual(output, "** invalid dictionary syntax **")

    def test_emptyline(self):
        """
        Test empty line.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_eof(self):
        """
        Test EOF command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("EOF")
            output = f.getvalue().strip()
            self.assertEqual(output, "")


if __name__ == '__main__':
    unittest.main()
