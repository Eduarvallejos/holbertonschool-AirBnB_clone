#!/usr/bin/python3
"""Definimos la clase HBNBCommand."""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Interprete de comandos"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Salir del programa"""
        return True

    def do_EOF(self, arg):
        """Salir del programa"""
        return True
    
    def emptyline(self):
        """No haga nada en una línea vacía"""
        pass

    def do_create(self, arg):
        """Crea una nueva instancia de BaseModel, la guarda (en el archivo JSON) e imprime el ID."""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
