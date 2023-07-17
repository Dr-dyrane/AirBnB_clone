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
    (hbnb) show User 1234-1234-1234
    (hbnb) all
    (hbnb) update Place 9876 name "New Place"
For more information on available commands, type 'help'.
Authors: Ukpono Umoren & Alexander Udeogaranya
"""

import cmd
import re
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    The HBnB command-line interpreter.
    The HBNBCommand class represents the command-line interpreter for
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
        FileStorage().new(new_instance)
        FileStorage().save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance.
        Usage: show <class_name> <instance_id>
        Example:
            (hbnb) show User 1234-1234-1234
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance = FileStorage().get(self.classes[args[0]], instance_id)
        if instance is None:
            print("** no instance found **")
            return
        print(instance)

    def do_destroy(self, arg):
        """
        Delete an instance.
        Usage: destroy <class_name> <instance_id>
        Example:
            (hbnb) destroy User 1234-1234-1234
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance = FileStorage().get(self.classes[args[0]], instance_id)
        if instance is None:
            print("** no instance found **")
            return
        FileStorage().delete(instance)
        FileStorage().save()

    def do_all(self, arg):
        """
        Retrieve all instances or instances of a specific class.
        Usage: all [class_name]
        Example:
            (hbnb) all
            (hbnb) all User
        """
        args = arg.split()
        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            objects = FileStorage().all()
            for obj in objects.values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    obj_list.append(str(obj))
                elif len(args) == 0:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_count(self, arg):
        """
        Count the number of instances of a class.
        Usage: count <class_name>
        Example:
            (hbnb) count User
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        count = FileStorage().count(self.classes[args[0]])
        print(count)

    def do_update(self, arg):
        """
        Update an instance with new attribute values.
        Usage:
        update <class_name> <instance_id> <attribute_name> "<attribute_value>"
        update <class_name> <instance_id> <dictionary>
        Example:
        (hbnb) update User 1234-1234-1234 first_name "John"
        (hbnb) update User 1234-1234-1234 {"age": 30, "city": "San Francisco"}
        """
        args = arg.split(maxsplit=3)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance = FileStorage().get(self.classes[args[0]], instance_id)
        if instance is None:
            print("** no instance found **")
            return
        if len(args) == 2 and args[2].startswith("{") and args[2].endswith("}"):
            try:
                attributes = json.loads(args[2].replace("'", "\""))
            except json.JSONDecodeError:
                print("** invalid dictionary syntax **")
                return
            for attr, value in attributes.items():
                setattr(instance, attr, value)
        elif len(args) >= 3:
            setattr(instance, args[2], self.parse_attribute_value(args[3]))
        else:
            print("** invalid syntax **")
            return
        FileStorage().save()

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
