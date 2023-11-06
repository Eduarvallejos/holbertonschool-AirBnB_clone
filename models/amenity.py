#!/usr/bin/python3
"""Se define la clase 'Amenity'."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representa el servicio.

    Attributes:
        name (str): El nombre del servicio.
    """

    name = ""
