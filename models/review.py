#!/usr/bin/python3
"""Se define la clase 'Review'."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representa una reseña.

    Attributes:
        place_id (str): id del lugar.
        user_id (str): id del usuario.
        text (str): El texto de la reseña.
    """

    place_id = ""
    user_id = ""
    text = ""
