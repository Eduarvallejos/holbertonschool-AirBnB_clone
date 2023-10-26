#!/usr/bin/python3
"""
Este modulo representa una clase BaseModel.
"""
import uuid
import datetime


class BaseModel:
    def __init__(self):
        """
        Inicializa una instancia de BaseModel.

        Args:

        Self.id: Genera un ID único utilizando uuid4 y
        lo convierte en una cadena.

        Self.created_at: Establece la fecha y hora de creación
        al momento actual en formato ISO.

        Self.updated_at: Establece la fecha y hora de actualización
        al momento actual en formato ISO.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        """Devuelve una representación de cadena del objeto."""
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Actualiza el atributo updated_at con la fecha y hora actual."""
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """Devuelve un diccionario con los atributos del objeto."""
        self.__dict__["__class__"] = "BaseModel"
        return self.__dict__
