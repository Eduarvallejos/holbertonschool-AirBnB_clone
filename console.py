#!/usr/bin/python3
"""Definimos la clase HBNBCommand."""
import cmd
import shlex
from models import storage
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
        """
        Crea una nueva instancia de BaseModel;
        la guarda (en el archivo JSON) e imprime el ID.
        """
        if not arg:
            print("** class name missing **")
        elif arg not in storage.classes:
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = shlex.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = args[1]
            obj = storage.get(args[0], obj_id)
            if obj in None:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, arg):
        """
        Destroy an instance based on the class name and id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = args[1]
            obj = storage.get(args[0], obj_id)
            if obj is None:
                print("** no instance found **")
            else:
                storage.delete(obj)
                storage.save()

    def do_all(self, arg):
        """
        Imprimir todas las instancias o instancias de una clase específica.
        """
        args = shlex.split(arg)
        if not arg or not args:
            objetos = storage.all()
        elif args[0] not in storage.classes:
            print("** la clase no existe **")
            return
        else:
            objetos = storage.all(args[0])
        print([str(obj) for obj in objetos.values()])

    def do_update(self, arg):
        """
        Actualizar una instancia basada en el nombre de la clase y el id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            class_name = args[0]
            obj_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]

            obj = storage.get(class_name, obj_id)
            if obj is None:
                print("** no instance found **")
            else:
                """
                Verificar que el atributo no sea 'id', 'created_at' o
                'updated_at'
                """
                if attribute_name not in ['id', 'created_at', 'updated_at']:
                    """
                    Convertir el valor del atributo al tipo apropiado.
                    """
                    if hasattr(obj, attribute_name):
                        setattr(obj, attribute_name, attribute_value)
                        obj.save()
                else:
                    print("** el atributo no puede ser actualizado **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
