#!/usr/bin/python3
"""The console | console 0.0.1"""
import cmd


class HBNBCommand(cmd.Cmd):
    """A command interpreter for the console.py"""

    prompt = "(hbnb) "

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
