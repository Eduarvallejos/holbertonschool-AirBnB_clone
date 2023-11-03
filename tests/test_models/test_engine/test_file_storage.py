#!/usr/bin/python3
import unittest
from unittest.mock import mock_open, patch
from models.engine.file_storage import FileStorage  

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()

    def test_all_returns_empty_dict_initially(self):
        objects = self.file_storage.all()
        self.assertEqual(objects, {})

    def test_new_adds_object_to_objects_dict(self):
        class DummyObject:
            def __init__(self, id):
                self.id = id

        dummy_obj = DummyObject("123")
        self.file_storage.new(dummy_obj)
        objects = self.file_storage.all()
        self.assertIn('DummyObject.123', objects)

    @patch('builtins.open', new_callable=mock_open)
    def test_save_serializes_objects_to_json_file(self, mock_file_open):
        class DummyObject:
            def __init__(self, id):
                self.id = id
            def to_dict(self):
                return {'id': self.id}

        dummy_obj = DummyObject("123")
        self.file_storage.new(dummy_obj)
        self.file_storage.save()

        # Verify that the 'open' function was called with the correct arguments
        mock_file_open.assert_called_with('file.json', 'w')
        handle = mock_file_open()
        handle.write.assert_called_with('{"DummyObject.123": {"id": "123"}}')

    @patch('builtins.open', new_callable=mock_open, read_data='{"DummyObject.123": {"id": "123"}}')
    def test_reload_deserializes_json_file_to_objects(self, mock_file_open):
        self.file_storage.reload()
        objects = self.file_storage.all()
        self.assertIn('DummyObject.123', objects)

if __name__ == '__main__':
    unittest.main()
