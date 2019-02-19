#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """this class is the beginning of the interpreter"""
    prompt = "(hbnb) "
# adding the classes to this list so the methods check throgh here if class
# exists.

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF():
        """End of File to exit file."""
        print()

    def emptyline(self):
        """method so it should not execute anything"""
        pass

    def do_create(self, *args):
        """Creates new instance of BaseModel & saves to json file & prints
        id"""
        if args < 1:
            print("** class name missing **")
        if args[0] not in self.list_classes:
            print("** class doesn't exist **")
        newinstance = BaseModel()
        newinstance.save()
        print(newinstance.id)

    def do_show():
        """prints the str rep. of an instance based on the class and id."""

    def do_destroy():
        """deletes an instance based on the class name and id, must save the
        change in the JSON file)"""

    def do_all():
        """prints all string representation of all instances based or not on the
        class name"""

    def do_update():
        """update/adds attributes in an instance based on class and id."""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
