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
        Devuelve el diccionario de todos los objetos.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Agrega un objeto al diccionario __objects.

        Args:
            obj: El objeto a agregar.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializa __objects en el archivo JSON.
        """
        data = {}
        for k, obj in FileStorage.__objects.items():
            data[k] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """
        Deserializa el archivo JSON a __objects (si existe).
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objeto_rec= json.load(f)
                for k, v in objeto_rec.items():
                    from models.base_model import BaseModel

                    FileStorage.__objects[k] = BaseModel(**v)
        except FileNotFoundError:
            return
