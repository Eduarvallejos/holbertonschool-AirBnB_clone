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
        Prueba si el método new() agrega un objeto al diccionario __objects.
        """
        class DummyObject:
            def __init__(self, id):
                self.id = id

        dummy_obj = DummyObject("123")
        self.file_storage.new(dummy_obj)
        objects = self.file_storage.all()
        self.assertIn('DummyObject.123', objects)

    @patch('builtins.open', new_callable=mock_open)
    def test_save(self, mock_file_open):
        """
        Prueba si el método save() serializa objetos en un archivo JSON.
        """
        class DummyObject:
        class DummyObject:
            def __init__(self, id):
                self.id = id
            def to_dict(self):
                return {'id': self.id}

        dummy_obj = DummyObject("123")
        self.file_storage.new(dummy_obj)
        self.file_storage.save()

        """
        Verifica que la función 'open' se llamó con los argumentos correctos.
        """
        mock_file_open.assert_called_with('file.json', 'w')
        handle = mock_file_open()
        handle.write.assert_called_with('{"DummyObject.123": {"id": "123"}}')

    @patch('builtins.open', new_callable=mock_open, read_data='{"DummyObject.123": {"id": "123"}}')
    def test_reload(self, mock_file_open):
        """
        Prueba si el método reload() deserializa un archivo JSON en objetos.
        """
        self.file_storage.reload()
        objects = self.file_storage.all()
        self.assertIn('DummyObject.123', objects)

if __name__ == '__main__':
    unittest.main()
