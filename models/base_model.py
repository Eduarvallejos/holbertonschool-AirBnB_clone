#!/usr/bin/python3
"""
Este modulo representa una clase BaseModel.
"""
import uuid
import datetime


class BaseModel:
    """
    Este es una clase que define BaseModel.
    """
    def __init__(self):
        """
        Genera un ID único utilizando uuid4 y lo convierte en una cadena.
        """
        self.id = str(uuid.uuid4())
        """
        Establece la fecha y hora de creación al momento actual en formato ISO.
        """
        self.created_at = datetime.datetime.now().isoformat()
        """
        Establece la fecha y hora de actualización al momento actual
        en formato ISO.
        """
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        """
        Devuelve una representación en cadena del objeto.
        Incluye el nombre de la clase, el ID y los atributos del objeto.
        """
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Actualiza la fecha y hora de actualización al momento actual
        en formato ISO.
        """
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """
        Agrega el nombre de la clase al diccionario y devuelve
        todos los atributos en un diccionario.
        """
        self.__dict__["__class__"] = "BaseModel"
        return self.__dict__
