#!/usr/bin/python3
"""
Este modulo representa una clase BaseModel.
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Inicializa una instancia de BaseModel.

        Atributos:

        Id: Genera un ID único utilizando uuid4 y
        lo convierte en una cadena.

        Created_at: Establece la fecha y hora de creación
        al momento actual en formato ISO.

        Updated_at: Establece la fecha y hora de actualización
        al momento actual en formato ISO.

        Args:
            **Kwargs: Resibe un diccionario:
        """
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
            
            self.__dict__["created_at"] = datetime.strptime(
                self.__dict__["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__["updated_at"] = datetime.strptime(
                self.__dict__["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Devuelve una representación de cadena del objeto."""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Actualiza el atributo updated_at con la fecha y hora actual."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Devuelve un diccionario con los atributos del objeto."""
        
        my_dict['created_at'] = self.__dict__['created_at'].isoformat()
        my_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
