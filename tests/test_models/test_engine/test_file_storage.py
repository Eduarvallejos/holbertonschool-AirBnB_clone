#!/usr/bin/python3
import unittest


class TestStorage(unittest.TestCase):
    def test_file_path(self):
        self.assertIsNone(FileStorage.__file_path)
