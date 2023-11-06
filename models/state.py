#!/usr/bin/python3
"""Se define la clase 'state'."""
from models.base_model import BaseModel


class State(BaseModel):
    """Representa a un estado.

    Attributes:
        name (str): El nombre del estado.
    """

    name = ""
