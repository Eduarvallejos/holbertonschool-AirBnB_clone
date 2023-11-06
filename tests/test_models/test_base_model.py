#!/usr/bin/python3
"""
Este modulo ase un test a nuestra clase BaseModel
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Esta clase define los casos de prueba
    """
    def test_init(self):
        """Prueba que se genere un ID único y que las fechas de creación y
        actualización se establezcan correctamente.
        """
        model = BaseModel()
        self.assertTrue(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_save(self):
        """
        Prueba que el método save actualice la fecha de actualización.
        """
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        new_updated_at = model.updated_at
        self.assertGreater(new_updated_at, original_updated_at)

    def test_to_dict(self):
        """
        Prueba que el método to_dict devuelva un diccionario
        con los atributos correctos.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIn("__class__", model_dict)

    def test_str(self):
        """
        Prueba que el método __str__ devuelva una representación
        en cadena válida del objeto.
        """
        model = BaseModel()
        self.assertEqual(
                str(model), f"[BaseModel] ({model.id}) {model.__dict__}")


if __name__ == "__main__":
    unittest.main()
