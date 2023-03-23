#!/usr/bin/python3
"""Command Line Interface for Airbnb"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """Command Line Interface for Airbnb"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it to JSON file and prints the id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            instance = classes[args[0]]()
            instance.save()
            print(instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            instance = storage.all()[args[0] + '.' + args[1]]
            print(instance)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id,
        and saves the change into the JSON file"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            instance = storage.all()[args[0] + '.' + args[1]]
            instance.delete()
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        objects = []
        try:
            args = arg.split()
            if args[0] in classes:
                for k, v in storage.all().items():
                    if args[0] in k:
                        objects.append(str(v))
            else:
                print("** class doesn't exist **")
                return
        except IndexError:
            for k, v in storage.all().items():
                objects.append(str(v))
        print(objects)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute and saves the change
        into the JSON file"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            instance = storage.all()[args[0] + '.' + args[1]]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(instance, args[2], args[3])
            instance.save()
        except KeyError:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().
