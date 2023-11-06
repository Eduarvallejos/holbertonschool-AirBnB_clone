#!/usr/bin/python3
"""Defines the FileStorage class."""
import json


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retorna el contenido de .__objects.
        Returns:
            dict
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
            with open(FileStorage.__file_path, 'r') as json_file:
                objeto_rec = json.load(json_file)
                for k, v in objeto_rec.items():
                    from models.base_model import BaseModel
                    FileStorage.__objects[k] = BaseModel(**v)
        except FileNotFoundError:
            return

    def attributes(self):
        """Devuelve un diccionario de atributos para diferentes clases."""
        attributes = {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
                 },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
                 },
        }
        return attributes
