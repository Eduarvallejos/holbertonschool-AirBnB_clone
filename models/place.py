#!/usr/bin/python3
"""Se define la clase 'Place'."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Representa el lugar.

    Attributes:
        city_id (str): id de la ciudad.
        user_id (str): id del usuario.
        name (str): El nombre del lugar.
        description (str): descripcion del lugar.
        number_rooms (int): El numero de habitaciones.
        number_bathrooms (int): El numero de baños.
        max_guest (int): El numero maximo de huespedes.
        price_by_night (int): El precio por noche.
        latitude (float): La latitud del lugar.
        longitude (float): La longitud del lugar.
        amenity_ids (list): Una lista de los servicios.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
