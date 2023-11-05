#!/usr/bin/python3
"""Definimos la clase HBNBCommand."""
import cmd


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
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.__classes[arg]()
            new_instance.save()
            print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
