#!/usr/bin/python3
"""Definimos la clase HBNBCommand."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel


def parse(arg):
    dot1 = re.search(r"\{(.*?)\}", arg)
    dot2 = re.search(r"\[(.*?)\]", arg)
    if dot1 is None:
        if dot2 is None:
            return [i.strip(",") for i in split(arg)]
        else:
            hbn = split(arg[:dot2.span()[0]])
            retl = [i.strip(",") for i in hbn]
            retl.append(dot2.group())
            return retl
    else:
        hbn = split(arg[:dot1.span()[0]])
        retl = [i.strip(",") for i in hbn]
        retl.append(dot1.group())
        return retl

class HBNBCommand(cmd.Cmd):
    """Interprete de comandos"""
    prompt = "(hbnb) "

    def default(self, arg):
        """Sintaxis por defecto del modulo cmd si la entrada no es valida"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))

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
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Print the string representation of an instance"""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

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
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """
        Actualizar una instancia basada en el nombre de la clase y el id.
        """
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
