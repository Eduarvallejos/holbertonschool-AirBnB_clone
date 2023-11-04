#!/usr/bin/python3
import cmd
"""Define la clase HBNBCommand."""


class HBNBCommand(cmd.Cmd):
    """Esta clase hereda de cmd.cmd."""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Salir de la consola HBNB."""
        return True

    def do_EOF(self, arg):
        """Señal EOF para salir del programa"""
        print()
        return True

    def emtyline(self):
        """No hace nada al resibir una linea vacia."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
