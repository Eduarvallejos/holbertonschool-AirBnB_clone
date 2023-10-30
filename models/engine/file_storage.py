#!/usr/bin/python3
import datetime
import json
from os import path
"""
Se difine una class llamada FileStorage.
"""


class FileStorage:
    """
    Clase que gestiona el almacenamiento de objetos en un archivo JSON.
    """
    __file_path = "file.json"
    __objects = {}    

    def all(self):
        """
        Devuelve todos los objetos almacenados.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Agrega un nuevo objeto al almacenamiento.

        Args:
            obj: El objeto a agregar.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Guarda los objetos en el archivo JSON.
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """
        Carga los objetos desde el archivo JSON y los almacena en el almacenamiento.
        """
        if path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
                FileStorage.__objects = obj_dict
