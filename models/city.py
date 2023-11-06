#!/usr/bin/python3
"""Se define la clase 'City'."""
from models.base_model import BaseModel


class City(BaseModel):
    """ Define el nombre de la ciudad.

    Atributos:
        name(str): Nombre de la ciudad.
        state_id (str): id del estado.
    """

    state_id = ""
    name = ""
