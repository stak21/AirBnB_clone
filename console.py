#!/usr/bin/python3
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """this class is the beginning of the interpreter"""
    prompt = "(hbnb) "
    list_classes = [
                "BaseModel",
                "User",
                "Place",
                "State",
                "City",
                "Amenity",
                "Review"
                ]

    def precmd(self, line):
        storage.reload()
        regex = "[^()., {:\"}']+"
        matches = re.finditer(regex, line, re.MULTILINE)
        all_group = []
        cmd = cls = uid = ""
        for match in matches:
            all_group.append(match.group())
        if len(all_group) == 1:
            return line
        elif len(all_group) == 2:  # assigns only if correct number of args
            cmd = all_group.pop(0)
            cls = all_group.pop(0)
        elif len(all_group) >= 3:
            cmd = all_group.pop(0)
            cls = all_group.pop(0)
            uid = all_group.pop(0)
        else:
            return line
        if '.' in line:
            cmd, cls = cls, cmd
        line = "{} {}".format(cmd, cls)
        if cmd == "update":
            if len(all_group) > 1:
                for key, value in zip(all_group[0::2], all_group[1::2]):
                    self.do_update(cls, uid, key, value)
                return ""
            else:
                if uid:
                    line += " " + uid
                if all_group:
                    line += " " + all_group[0]
                return line
        if cls in self.list_classes:
            line = "{} {} {}".format(cmd, cls, uid)
        return line

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, args):
        """End of File to exit file."""
        return True

    def emptyline(self):
        """method so it should not execute anything"""
        pass

    def do_count(self, *args):
        """ counts the number of instances of a given class """
        count = 0
        args = [ele for ele in args[0].split(' ')]
        if args[0] == '':
            print("** class name missing **")
            return
        if args[0] not in self.list_classes:
            print("** class doesn't exist **")
            return
        else:
            ''' Get a list of specified instances '''
            for key, obj in storage.all().items():
                key = key.split('.')
                if key[0] == args[0]:
                    count += 1
            print(count)

    def do_create(self, *args):
        """Creates new instance of BaseModel & saves to json file & prints
        id"""
        """ args without commas created a tuple of 1, so I created a list with
        the tuple being split by spaces  """
        args = [ele for ele in args[0].split(' ')]
        if args[0] == '':
            print("** class name missing **")
            return
        if args[0] not in self.list_classes:
            print("** class doesn't exist **")
            return
        newinstance = eval("{}()".format(args[0]))
        newinstance.save()
        print(newinstance.id)

    def do_show(self, *args):
        """prints the str rep. of an instance based on the class and id."""
        args = [ele for ele in args[0].split(' ')]
        if args[0] == '':
            print("** class name missing **")
            return
        if args[0] not in self.list_classes:
            print("** class doesn't exist **")
            return
        if len(args) != 2:
            print("** instance id missing **")
            return

        storage.reload()
        dict_objs = storage.all()
        if dict_objs is None or dict_objs == []:
            print("** no instance found **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key in dict_objs.keys():
            print(dict_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, *args):
        """deletes an instance based on the class name and id, must save the
        change in the JSON file)"""
        args = [ele for ele in args[0].split(' ')]
        if args[0] == '':
            print("** class name missing **")
            return
        if args[0] not in self.list_classes:
            print("** class doesn't exist **")
            return
        if len(args) != 2:
            print("** instance id missing **")
            return

        storage.reload()
        dict_objs = storage.all()
        if dict_objs is None or dict_objs == []:
            print("** no instance found **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key in dict_objs.keys():
            del dict_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, *args):
        """prints all string representation of all instances based or not on the
        class name"""
        args = [ele for ele in args[0].split(' ')]
        print_obj = []
        storage.reload()
        if args[0] == '':
            for key, obj in storage.all().items():
                print_obj.append(obj.__str__())
            print(print_obj)
            return
        if args[0] not in self.list_classes:
            print("** class doesn't exist **")
            return
        else:
            ''' Get a list of specified instances '''
            for key, obj in storage.all().items():
                key = key.split('.')
                if key[0] == args[0]:
                    print_obj.append(obj.__str__())
            print(print_obj)

    def do_update(self, *args):
        """update/adds attributes in an instance based on class and id."""
        if len(args) == 1:
            args = [ele for ele in args[0].split(' ')]
        if args[0] == '':
            print("** class name missing **")
            return
        if args[0] not in self.list_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return

        storage.reload()
        dict_objs = storage.all()
        if dict_objs is None or dict_objs == []:
            print("** no instance found **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key in dict_objs.keys():
            obj = dict_objs[key]
            if args[2] in obj.__class__.__dict__:
                obj.__dict__[args[2]] =\
                    type(obj.__class__.__dict__[args[2]])(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
            storage.save()
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
