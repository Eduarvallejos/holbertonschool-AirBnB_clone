#!/usr/bin/python3
import datetime
import json
from models.base_model import BaseModel
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
        Devuelve el diccionario de todos los objetos.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Agrega un objeto al diccionario __objects.

        Args:
            obj: El objeto a agregar.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """
        Serializa __objects en el archivo JSON.
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """
        Deserializa el archivo JSON a __objects (si existe).
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
