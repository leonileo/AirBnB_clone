#!/usr/bin/python3
"""The console | console 0.0.1"""
import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """A command interpreter for the console.py"""

    prompt = "(hbnb) "

    def do_create(self, model):
        """Create a new instance of BaseModel and saves it to a JSON file."""
        if not model:
            print("** class name missing **")
        elif model != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance,
        base on the class name and id."""
        args = args.split()

        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
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
        elif args[0] != "BaseModel":
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

    def do_all(self, args):
        """Print all instance of a model."""
        if args and args != "BaseModel":
            print("** class doesn't exist **")

        objs = storage.all()
        result = []
        for key, obj in objs.items():
            if not args or key.startswith(args):
                result.append(str(obj))
        print(result)

    def do_update(self, args):
        """ Updates an instance. """
        args = args.split()

        if not args:
            print("** class name missing **")

        elif args[0] != "BaseModel":
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
