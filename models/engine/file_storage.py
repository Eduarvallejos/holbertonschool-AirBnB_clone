#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
<<<<<<< HEAD
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)
=======
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
>>>>>>> 83f866909f622c792342af2f853e597835626745

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
<<<<<<< HEAD
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
=======
            with open(FileStorage.__file_path, 'r') as json_file:
                objeto_rec= json.load(json_file)
                for k, v in objeto_rec.items():
                    from models.base_model import BaseModel
                    FileStorage.__objects[k] = BaseModel(**v)
>>>>>>> 83f866909f622c792342af2f853e597835626745
        except FileNotFoundError:
            return
