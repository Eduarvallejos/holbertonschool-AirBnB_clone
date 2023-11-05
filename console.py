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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
