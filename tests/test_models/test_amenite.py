import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_attributes(self):
        """
        Verificar que los atributos de Amenity se inicializan correctamente.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertIsInstance(amenity.name, str)

    def test_inheritance(self):
        """Verificar que Amenity hereda de BaseModel."""
        amenity = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == "__main__":
    unittest.main()
