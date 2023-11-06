#!/usr/bin/python3
"""Se define la clese 'User'."""
from models.base_model import BaseModel


class User(BaseModel):
    """Representa un usuario.

    Attributes:
        email (str): El correo electronico del usuario.
        password (str): La contraseña del usuario.
        first_name (str): El primer nombre del usuario.
        last_name (str): el apellido del usuario.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
