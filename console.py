#!/usr/bin/python3
"""The console | console 0.0.1"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """A command interpreter for the console.py"""

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }
    
    def do_create(self, arg):
        """Create a new instance of BaseModel and saves it to a JSON file."""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance,
        base on the class name and id."""
        args = args.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, args):
        """Deletes an instance."""
        args = args.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class dosen't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])

            if key not in storage.all():
                print("** no instance found**")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Print all instance of a model."""
        if arg and arg not in self.classes:
            print("** class doesn't exist **")

        else:        
            result = []
            for obj in storage.all().values():
                if not arg or obj.__class__.__name__ == arg:
                    result.append(str(obj))
            print(result)

    def do_update(self, args):
        """ Updates an instance. """
        args = args.split()

        if not args:
            print("** class name missing **")

        elif args[0] not in self.classes:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            key = "{}.{}".format(args[0], args[1])
            obj = storage.all().get(key)

            if obj is None:
                print("** no instance found **")

            elif len(args) < 3:
                print("** attribute name missing **")

            elif len(args) < 4:
                print("** value missing **")

            else:
                attr_name = args[2]
                attr_value = args[3]
                try:
                    if "." in attr_value:
                        attr_value = float(attr_value)
                    else:
                        attr_value = int(attr_value)
                except ValueError:
                    attr_value = attr_value.strip('"')
                setattr(obj, attr_name, attr_value)
                obj.save()

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
