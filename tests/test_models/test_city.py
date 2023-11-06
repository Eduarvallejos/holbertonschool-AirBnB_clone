#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def test_attributes(self):
        """
        Verificar que los atributos de City se inicializan correctamente.
        """
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.state_id, str)

    def test_inheritance(self):
        """Verificar que City hereda de BaseModel."""
        city = City()
        self.assertTrue(issubclass(City, BaseModel))


if __name__ == "__main__":
    unittest.main()
