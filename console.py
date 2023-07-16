#!/usr/bin/python3
"""
This module defines the HBnB console;

A command-line interface for interacting
with the HolbertonBnB application.

The console allows users to create, retrieve, update, and delete objects
in the application's storage system.

It supports various commands for managing different types of objects,
such as BaseModel, User, State, City, Place, Amenity, and Review.

Usage:
    $ ./console.py

Command examples:
    (hbnb) create BaseModel
    (hbnb) show User 12345
    (hbnb) all
    (hbnb) update Place 9876 name "New Place"

For more information on available commands, type 'help'.

Authors: Ukpono Umoren & Alexander Udeogaranya
"""

import cmd
import re
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    The HBnB command-line interpreter.

    The HBNBCommand class represents the command-line interpreter for;
    the HolbertonBnB application.
    It inherits from the cmd.Cmd class provided by the cmd module,
    which provides a framework for
    creating command-line interpreters.

    Attributes:
        prompt (str): The command prompt.
        classes (dict): A dictionary of available model classes.
    """

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def emptyline(self):
        """
        Called when an empty line is entered. Does nothing.
        """
        pass

    def default(self, line):
        """
        Called when the entered command is not recognized.

        Args:
            line (str): The entered command line.
        """
        print("*** Unknown syntax: {}".format(line))

    def do_quit(self, arg):
        """
        Quit the console.

        Usage: quit | exit
        """
        return True

    def do_EOF(self, arg):
        """
        Handle the End-of-File (EOF) signal to exit the console.

        Usage: EOF
        """
        print("")  # Print a new line before exiting
        return True

    def do_create(self, arg):
        """
        Create a new instance of a model class.

        Usage: create <class_name>

        Example:
            (hbnb) create User
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance.

        Usage: show <class_name> <instance_id>

        Example:
            (hbnb) show User 12345
        """
        args = arg.split()
        if len(args) != 2:
            print("** invalid number of arguments **")
            return

        class_name = args[0]
        instance_id = args[1]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, instance_id)
        instance = storage.get(class_name, instance_id)
        if instance is None:
            print("** no instance found **")
            return

        print(instance)

    def do_destroy(self, arg):
        """
        Delete an instance.

        Usage: destroy <class_name> <instance_id>

        Example:
            (hbnb) destroy User 12345
        """
        args = arg.split()
        if len(args) != 2:
            print("** invalid number of arguments **")
            return

        class_name = args[0]
        instance_id = args[1]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, instance_id)
        instance = storage.get(class_name, instance_id)
        if instance is None:
            print("** no instance found **")
            return

        storage.delete(instance)
        storage.save()

    def do_all(self, arg):
        """
        Retrieve all instances or instances of a specific class.

        Usage: all [class_name]

        Example:
            (hbnb) all
            (hbnb) all User
        """
        args = arg.split()
        if len(args) > 1:
            print("** invalid number of arguments **")
            return

        if len(args) == 1 and args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        instances = []
        if len(args) == 0:
            instances = storage.all().values()
        else:
            instances = storage.all(args[0]).values()

        print([str(instance) for instance in instances])

    def do_update(self, arg):
        """
        Update an instance with new attribute values.

        Usage:
        update <class_name> <instance_id> <attribute_name> <attribute_value>
        update <class_name> <instance_id> <dictionary>

        Example:
            (hbnb) update User 12345 first_name "John"
            (hbnb) update User 12345 {"age": 30, "city": "San Francisco"}
        """
        args = arg.split(maxsplit=3)
        if len(args) < 3:
            print("** invalid number of arguments **")
            return

        class_name = args[0]
        instance_id = args[1]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, instance_id)
        instance = storage.get(class_name, instance_id)
        if instance is None:
            print("** no instance found **")
            return

        if len(args) == 3:
            # Update a single attribute
            attribute_name = args[2]
            attribute_value = parse_attribute_value(args[3])
            setattr(instance, attribute_name, attribute_value)
        elif len(args) == 2 and args[2].startswith("{") and args[2].endswith("}"):
            # Update multiple attributes using a dictionary
            try:
                attributes = json.loads(args[2].replace("'", "\""))
            except json.JSONDecodeError:
                print("** invalid dictionary syntax **")
                return

            for attribute_name, attribute_value in attributes.items():
                setattr(instance, attribute_name,
                        parse_attribute_value(attribute_value))
        else:
            print("** invalid syntax **")
            return

        instance.save()
        print(instance)

    def do_count(self, arg):
        """
        Count the number of instances of a class.

        Usage: count <class_name>

        Example:
            (hbnb) count User
        """
        args = arg.split()
        if len(args) != 1:
            print("** invalid number of arguments **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        count = storage.count(class_name)
        print(count)

    # Helper function to parse attribute values


@staticmethod
def parse_attribute_value(value):
    """
    Parse the attribute value and convert it to the appropriate data type.

    Args:
        value (str): The attribute value as a string.

    Returns:
        The parsed attribute value as the appropriate data type.
    """
    try:
        parsed_value = json.loads(value)
    except json.JSONDecodeError:
        # If JSON decoding fails, return the original string value
        return value

    return parsed_value


# Run the console
if __name__ == "__main__":
    HBNBCommand().cmdloop()
