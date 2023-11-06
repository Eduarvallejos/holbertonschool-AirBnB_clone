#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def test_attributes(self):
        """
        Verificar que los atributos de User se inicializan correctamente.
        """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_inheritance(self):
        """Verificar que User hereda de BaseModel."""
        user = User()
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == "__main__":
    unittest.main()
