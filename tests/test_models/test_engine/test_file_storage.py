#!/usr/bin/python3
import unittest
from unittest.mock import mock_open, patch
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """
        Preparación para las pruebas: crea una instancia de FileStorage.
        """
        self.file_storage = FileStorage()

    def test_all(self):
        """
        Prueba si el método all() devuelve un diccionario vacío inicialmente.
        """
        objects = self.file_storage.all()
        self.assertEqual(objects, {})

    def test_new(self):
        """
        Prueba si el método new() agrega un objeto al diccionario '__objects'.
        """
        storage = FileStorage()
        new_object = BaseModel()
        storage.new(new_object)
        self.assertIn(f"BaseModel.{new_object.id}", storage.all())

    def test_save_reload(self):
        """
        Prueba si el método 'save()' y 'reload()' funcionan correctamente.
        """
        storage = FileStorage()
        new_object = BaseModel()
        storage.new(new_object)
        storage.save()
        reloaded_storage = FileStorage()
        reloaded_storage.reload()
        self.assertIn(f"BaseModel.{new_object.id}", reloaded_storage.all())


if __name__ == "__main__":
    unittest.main()
