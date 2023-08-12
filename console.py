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
import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


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
        match = re.search(r"^(\w+)\.(\w+)\((.*)\)$", line)
        if match:
            class_name = match.group(1)
            method = match.group(2)
            method_args = match.group(3)
            self.handle_method(class_name, method, method_args)
        else:
            print("*** Unknown syntax: {}".format(line))

    def handle_method(self, class_name, method, method_args):
        """
        Handle method calls in the format <class_name>.<method>(<method_args>).
        Args:
            class_name (str): The name of the class.
            method (str): The name of the method.
            method_args (str): The arguments of the method.
        """
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if method == "all":
            self.handle_all(class_name)
        elif method == "count":
            self.handle_count(class_name)
        elif method == "show":
            instance_id = method_args.strip('\"\'')
            self.handle_show(class_name, instance_id)
        elif method == "destroy":
            instance_id = method_args.strip('\"\'')
            self.handle_destroy(class_name, instance_id)
        elif method == "update":
            if "{" in method_args and "}" in method_args:
                self.handle_update_with_dict(class_name, method_args)
            else:
                self.handle_update(class_name, method_args)
        else:
            print("** unknown method **")

    def handle_all(self, class_name):
        """
        Handle the "all" method to retrieve instances.
        Args:
            class_name (str): The name of the class.
        """
        obj_list = []
        objects = storage.all(self.classes[class_name])
        for obj in objects.values():
            obj_list.append(str(obj))
        print(obj_list)

    def handle_count(self, class_name):
        """
        Handle the "count" method to count instances.
        Args:
            class_name (str): The name of the class.
        """
        count = storage.count(self.classes[class_name])
        print(count)

    def handle_show(self, class_name, instance_id):
        """
        Handle the "show" method to retrieve an instance based on its ID.
        Args:
            class_name (str): The name of the class.
            instance_id (str): The ID of the instance.
        """
        instance = storage.get(self.classes[class_name], instance_id)
        if instance is None:
            print("** no instance found **")
        else:
            print(instance)

    def handle_destroy(self, class_name, instance_id):
        """
        Handle the "destroy" method to delete an instance based on its ID.
        Args:
            class_name (str): The name of the class.
            instance_id (str): The ID of the instance.
        """
        instance = storage.get(self.classes[class_name], instance_id)
        if instance is None:
            print("** no instance found **")
        else:
            storage.delete(instance)
            storage.save()

    def handle_update(self, class_name, update_args):
        """
        Handle the "update" method to update an instance's attributes.
        Args:
            class_name (str): The name of the class.
            update_args (str): The update arguments as a string.
        """
        args = update_args.split(",")
        if len(args) < 3:
            print("** missing arguments **")
            return

        instance_id = args[0].strip('\"\'')
        attribute_name = args[1].strip('\"\'')
        attribute_value = args[2].strip('\"\'')

        instance = storage.get(self.classes[class_name], instance_id)
        if instance is None:
            print("** no instance found **")
            return

        setattr(instance, attribute_name, attribute_value)
        setattr(instance, "updated_at", datetime.now())
        storage.save()

    def handle_update_with_dict(self, class_name, update_args):
        """
        Handle the "update" method to update an instance's attributes with a dictionary.
        Args:
            class_name (str): The name of the class.
            update_args (str): The update arguments as a string.
        """
        args = update_args.split(",", 1)
        if len(args) < 2:
            print("** missing arguments **")
            return

        instance_id = args[0].strip('\"\'')
        attribute_data = args[1].strip()

        try:
            attribute_dict = json.loads(attribute_data.replace("'", "\""))
        except json.JSONDecodeError:
            print("** invalid dictionary syntax **")
            return

        instance = storage.get(self.classes[class_name], instance_id)
        if instance is None:
            print("** no instance found **")
            return

        for attr, value in attribute_dict.items():
            parsed_value = self.parse_attribute_value(value)
            setattr(instance, attr, parsed_value)
        setattr(instance, "updated_at", datetime.now())
        storage.save()

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
        storage.new(new_instance)
        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance.
        Usage: show <class_name> <instance_id> <class_name>.show(<instance_id>)
        Example:
            (hbnb) show User 1234-1234-1234
            (hbnb) User.show("1234-1234-1234")
        """
        args = arg.split(".")
        if len(args) > 1:
            class_name = args[0]
            method = args[1]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            if method != "show":
                print("** unknown method **")
                return
            instance_id = args[2].strip('()')
            instance = storage.get(self.classes[class_name], instance_id)
            if instance is None:
                print("** no instance found **")
            else:
                print(instance)
        else:
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
            instance = storage.get(self.classes[args[0]], instance_id)
            if instance is None:
                print("** no instance found **")
                return
            print(instance)

    def do_destroy(self, arg):
        """
        Delete an instance.
        Usage: destroy <class_name> <instance_id>
        <class_name>.destroy(<instance_id>)
        Example:
            (hbnb) destroy User 1234-1234-1234
            (hbnb) User.destroy("1234-1234-1234")
        """
        args = arg.split(".")
        if len(args) > 1:
            class_name = args[0]
            method = args[1]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            if method != "destroy":
                print("** unknown method **")
                return
            instance_id = args[2].strip('()')
            instance = storage.get(self.classes[class_name], instance_id)
            if instance is None:
                print("** no instance found **")
            else:
                storage.delete(instance)
                storage.save()
        else:
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
            instance = storage.get(self.classes[args[0]], instance_id)
            if instance is None:
                print("** no instance found **")
                return
            storage.delete(instance)
            storage.save()

    def do_all(self, arg):
        """
        Retrieve all instances or instances of a specific class.
        Usage: all [class_name] or <class_name>.all()
        Example:
            (hbnb) all
            (hbnb) all User
            (hbnb) User.all()
        """
        args = arg.split(".")
        if len(args) > 1:
            class_name = args[0]
            method = args[1]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            if method != "all":
                print("** unknown method **")
                return
            obj_list = []
            objects = storage.all(self.classes[class_name])
            for obj in objects.values():
                obj_list.append(str(obj))
            print(obj_list)
        else:
            if len(args) > 0 and args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                obj_list = []
                objects = storage.all()
                for obj in objects.values():
                    if len(args) > 0 and args[0] == obj.__class__.__name__:
                        obj_list.append(str(obj))
                    elif len(args) == 0:
                        obj_list.append(str(obj))
                print(obj_list)

    def do_count(self, arg):
        """
        Count the number of instances of a class.
        Usage: count <class_name> or <class_name>.count()
        Example:
            (hbnb) count User
            (hbnb) User.count()
        """
        args = arg.split(".")
        if len(args) > 1:
            class_name = args[0]
            method = args[1]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            if method != "count":
                print("** unknown method **")
                return
            count = storage.count(self.classes[class_name])
            print(count)
        else:
            if len(args) > 0 and args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                count = storage.count(self.classes[args[0]])
                print(count)

    def do_update(self, arg):
        """
        Update an instance with new attribute values.
        Usage: update <class_name> <instance_id> <attribute_name>
            <attribute_value> or
            update <class_name> <instance_id> <dictionary representation> or
            <class_name>.update(<instance_id>, <dictionary representation>)
        Example:
            (hbnb) update User 1234-1234-1234 first_name "John"
            (hbnb) update User 1234-1234-1234
            {"age": 30, "city": "San Francisco"}
            (hbnb) User.update("1234-1234-1234",
            {"age": 30, "city": "San Francisco"})
        """
        args = arg.split(".")
        if len(args) > 1:
            class_name = args[0]
            method = args[1]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            if method != "update":
                print("** unknown method **")
                return
            update_args = args[2].strip('()')
            update_args = re.split(",\s*(?![^{}]*\})", update_args)
            instance_id = update_args[0].strip('\"\'')
            instance = storage.get(self.classes[class_name], instance_id)
            if instance is None:
                print("** no instance found **")
                return
            if len(update_args) < 2:
                print("** attribute dictionary missing **")
                return
            try:
                attribute_dict = json.loads(update_args[1].replace("'", "\""))
            except json.JSONDecodeError:
                print("** invalid dictionary syntax **")
                return
            for attr, value in attribute_dict.items():
                setattr(instance, attr, value)
            setattr(instance, "updated_at", datetime.now())
            storage.save()
        else:
            ags = arg.split(maxsplit=3)
            if len(ags) == 0:
                print("** class name missing **")
                return
            if ags[0] not in self.classes:
                print("** class doesn't exist **")
                return
            if len(ags) == 1:
                print("** instance id missing **")
                return
            instance_id = ags[1]
            instance = storage.get(self.classes[ags[0]], instance_id)
            if instance is None:
                print("** no instance found **")
                return
            if len(ags) == 2 and ags[2].startswith("{") and \
                    ags[2].endswith("}"):
                try:
                    attributes = json.loads(ags[2].replace("'", "\""))
                except json.JSONDecodeError:
                    print("** invalid dictionary syntax **")
                    return
                for attr, value in attributes.items():
                    setattr(instance, attr, value)
            elif len(ags) == 4:
                setattr(instance, ags[2], ags[3].strip("\""))
            else:
                print("** invalid syntax **")
                return
            storage.save()

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
