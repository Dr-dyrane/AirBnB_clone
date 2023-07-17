#!/usr/bin/python3
"""
ALX HolbertonBnB - Unit Tests for HBNBCommand

This module contains unit tests for the HBNBCommand class.

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    Test suite for the HBNBCommand class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.console = HBNBCommand()

    def tearDown(self):
        """
        Clean up after each test case.
        """
        self.console = None

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        """
        Test the help command.
        """
        self.console.onecmd("help")
        help_output = mock_stdout.getvalue()
        self.assertIn("Documented commands (type help <topic>):", help_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        """
        Test the quit command.
        """
        self.assertTrue(self.console.onecmd("quit"))
        quit_output = mock_stdout.getvalue()
        self.assertEqual("", quit_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        """
        Test the EOF command.
        """
        self.assertTrue(self.console.onecmd("EOF"))
        eof_output = mock_stdout.getvalue()
        self.assertEqual("", eof_output)

    def test_emptyline(self):
        """
        Test the emptyline command.
        """
        self.assertIsNone(self.console.emptyline())

    @patch('sys.stdout', new_callable=StringIO)
    def test_default(self, mock_stdout):
        """
        Test the default command.
        """
        self.console.default("invalid_command")
        default_output = mock_stdout.getvalue()
        self.assertIn("*** Unknown syntax:", default_output)

    def test_create(self):
        """
        Test the create command.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create"))
            create_output = mock_stdout.getvalue()
            self.assertEqual("** class name missing **\n", create_output)

            self.assertFalse(self.console.onecmd("create SomeClass"))
            create_output = mock_stdout.getvalue()
            self.assertEqual("** class doesn't exist **\n", create_output)

            self.assertTrue(self.console.onecmd("create BaseModel"))
            create_output = mock_stdout.getvalue()
            self.assertRegex(create_output, r"^\w{8}-.{4}-.{4}-.{4}-\w{12}\n$")

    def test_show(self):
        """
        Test the show command.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("show"))
            show_output = mock_stdout.getvalue()
            self.assertEqual("** class name missing **\n", show_output)

            self.assertFalse(self.console.onecmd("show SomeClass"))
            show_output = mock_stdout.getvalue()
            self.assertEqual("** class doesn't exist **\n", show_output)

            self.assertFalse(self.console.onecmd("show BaseModel"))
            show_output = mock_stdout.getvalue()
            self.assertEqual("** instance id missing **\n", show_output)

            self.assertFalse(self.console.onecmd(
                "show BaseModel 1234-1234-1234"))
            show_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", show_output)

    def test_destroy(self):
        """
        Test the destroy command.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("destroy"))
            destroy_output = mock_stdout.getvalue()
            self.assertEqual("** class name missing **\n", destroy_output)

            self.assertFalse(self.console.onecmd("destroy SomeClass"))
            destroy_output = mock_stdout.getvalue()
            self.assertEqual("** class doesn't exist **\n", destroy_output)

            self.assertFalse(self.console.onecmd("destroy BaseModel"))
            destroy_output = mock_stdout.getvalue()
            self.assertEqual("** instance id missing **\n", destroy_output)

            self.assertFalse(self.console.onecmd(
                "destroy BaseModel 1234-1234-1234"))
            destroy_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", destroy_output)

    def test_all(self):
        """
        Test the all command.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("all")
            all_output = mock_stdout.getvalue()
            self.assertEqual("[]\n", all_output)

            self.assertFalse(self.console.onecmd("all SomeClass"))
            all_output = mock_stdout.getvalue()
            self.assertEqual("** class doesn't exist **\n", all_output)

    def test_count(self):
        """
        Test the count command.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("count"))
            count_output = mock_stdout.getvalue()
            self.assertEqual("** class name missing **\n", count_output)

            self.assertFalse(self.console.onecmd("count SomeClass"))
            count_output = mock_stdout.getvalue()
            self.assertEqual("** class doesn't exist **\n", count_output)

    def test_update(self):
        """
        Test the update command.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("update"))
            update_output = mock_stdout.getvalue()
            self.assertEqual("** class name missing **\n", update_output)

            self.assertFalse(self.console.onecmd("update SomeClass"))
            update_output = mock_stdout.getvalue()
            self.assertEqual("** class doesn't exist **\n", update_output)

            self.assertFalse(self.console.onecmd("update BaseModel"))
            update_output = mock_stdout.getvalue()
            self.assertEqual("** instance id missing **\n", update_output)

            self.assertFalse(self.console.onecmd(
                "update BaseModel 1234-1234-1234"))
            update_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", update_output)

    def test_all_models_all(self):
        """
        Test all() method for all models.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("BaseModel.all()")
            all_output = mock_stdout.getvalue()
            self.assertEqual("[]\n", all_output)

            self.console.onecmd("User.all()")
            all_output = mock_stdout.getvalue()
            self.assertEqual("[]\n", all_output)

            self.console.onecmd("State.all()")
            all_output = mock_stdout.getvalue()
            self.assertEqual("[]\n", all_output)

            self.console.onecmd("City.all()")
            all_output = mock_stdout.getvalue()
            self.assertEqual("[]\n", all_output)

            self.console.onecmd("Amenity.all()")
            all_output = mock_stdout.getvalue()
            self.assertEqual("[]\n", all_output)

            self.console.onecmd("Place.all()")
            all_output = mock_stdout.getvalue()
            self.assertEqual("[]\n", all_output)

            self.console.onecmd("Review.all()")
            all_output = mock_stdout.getvalue()
            self.assertEqual("[]\n", all_output)

    def test_all_models_count(self):
        """
        Test count() method for all models.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("BaseModel.count()")
            count_output = mock_stdout.getvalue()
            self.assertEqual("0\n", count_output)

            self.console.onecmd("User.count()")
            count_output = mock_stdout.getvalue()
            self.assertEqual("0\n", count_output)

            self.console.onecmd("State.count()")
            count_output = mock_stdout.getvalue()
            self.assertEqual("0\n", count_output)

            self.console.onecmd("City.count()")
            count_output = mock_stdout.getvalue()
            self.assertEqual("0\n", count_output)

            self.console.onecmd("Amenity.count()")
            count_output = mock_stdout.getvalue()
            self.assertEqual("0\n", count_output)

            self.console.onecmd("Place.count()")
            count_output = mock_stdout.getvalue()
            self.assertEqual("0\n", count_output)

            self.console.onecmd("Review.count()")
            count_output = mock_stdout.getvalue()
            self.assertEqual("0\n", count_output)

    def test_all_models_show(self):
        """
        Test show() method for all models.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("BaseModel.show('id')")
            show_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", show_output)

            self.console.onecmd("User.show('id')")
            show_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", show_output)

            self.console.onecmd("State.show('id')")
            show_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", show_output)

            self.console.onecmd("City.show('id')")
            show_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", show_output)

            self.console.onecmd("Amenity.show('id')")
            show_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", show_output)

            self.console.onecmd("Place.show('id')")
            show_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", show_output)

            self.console.onecmd("Review.show('id')")
            show_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", show_output)

    def test_all_models_destroy(self):
        """
        Test destroy() method for all models.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("BaseModel.destroy('id')")
            destroy_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", destroy_output)

            self.console.onecmd("User.destroy('id')")
            destroy_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", destroy_output)

            self.console.onecmd("State.destroy('id')")
            destroy_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", destroy_output)

            self.console.onecmd("City.destroy('id')")
            destroy_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", destroy_output)

            self.console.onecmd("Amenity.destroy('id')")
            destroy_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", destroy_output)

            self.console.onecmd("Place.destroy('id')")
            destroy_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", destroy_output)

            self.console.onecmd("Review.destroy('id')")
            destroy_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", destroy_output)

    def test_all_models_update(self):
        """
        Test update() method for all models.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("BaseModel.update('id', 'name', 'test')")
            update_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", update_output)

            self.console.onecmd("User.update('id', 'name', 'test')")
            update_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", update_output)

            self.console.onecmd("State.update('id', 'name', 'test')")
            update_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", update_output)

            self.console.onecmd("City.update('id', 'name', 'test')")
            update_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", update_output)

            self.console.onecmd("Amenity.update('id', 'name', 'test')")
            update_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", update_output)

            self.console.onecmd("Place.update('id', 'name', 'test')")
            update_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", update_output)

            self.console.onecmd("Review.update('id', 'name', 'test')")
            update_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", update_output)

    def test_all_models_update_dict(self):
        """
        Test update() method with dictionary for all models.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("BaseModel.update('id', {'name': 'test'})")
            update_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", update_output)

            self.console.onecmd("User.update('id', {'name': 'test'})")
            update_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", update_output)

            self.console.onecmd("State.update('id', {'name': 'test'})")
            update_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", update_output)

            self.console.onecmd("City.update('id', {'name': 'test'})")
            update_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", update_output)

            self.console.onecmd("Amenity.update('id', {'name': 'test'})")
            update_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", update_output)

            self.console.onecmd("Place.update('id', {'name': 'test'})")
            update_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", update_output)

            self.console.onecmd("Review.update('id', {'name': 'test'})")
            update_output = mock_stdout.getvalue()
            self.assertEqual("** no instance found **\n", update_output)


if __name__ == '__main__':
    unittest.main()
