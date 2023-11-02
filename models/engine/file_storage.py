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
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """
        Serializa __objects en el archivo JSON.
        """
        data = {key: value for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as archivo:
            json.dump(FileStorage.__objects, archivo)

    def reload(self):
        """
        Deserializa el archivo JSON a __objects (si existe).
        """
        try:
            with open(FileStorage.__file_path, 'r') as archivo:
                data = json.load(archivo.read())
                FileStorage.__objects = data
        except FileNotFoundError:
            return
