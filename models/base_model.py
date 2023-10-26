#!/usr/bin/python3
"""
Este modulo representa una clase BaseModel.
"""
import uuid
from datetime import datetime



class BaseModel:
    def __init__(self):
        """
        Inicializa una instancia de BaseModel.

        Atributos:

        Self.id: Genera un ID único utilizando uuid4 y
        lo convierte en una cadena.

        Self.created_at: Establece la fecha y hora de creación
        al momento actual en formato ISO.

        Self.updated_at: Establece la fecha y hora de actualización
        al momento actual en formato ISO.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        """Devuelve una representación de cadena del objeto."""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Actualiza el atributo updated_at con la fecha y hora actual."""
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """Devuelve un diccionario con los atributos del objeto."""
        my_dict = dict(self.__dict__)
        my_dict['created_at'] = self.__dict__['created_at'].isoformat()
        my_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return (my_dict)
