#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = ["BaseModel"]

    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Empty line does nothing\n"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        Usage: create <class name>\n"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        Usage: show <class name> <id>\n"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            key = args[0] + '.' + args[1]
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
                return
            else:
                print(objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        Usage: destroy <class name> <id>\n"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            key = args[0] + '.' + args[1]
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
                return
            else:
                del objects[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        Usage: all, all <class name>\n"""
        args = arg.split()
        objects = storage.all()
        instance_list = []
        if len(args) == 0:
            for key in objects:
                instance_list.append(str(objects[key]))
            print(instance_list)
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for key in objects:
                if key.split('.')[0] ==
