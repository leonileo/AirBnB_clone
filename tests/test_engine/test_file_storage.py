#!/usr/bin/python3
"""Test for file_storage.py"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Unit test for the FileStorage class."""

    def setUp(self):
        """Set up resources before each test."""
        self.storage = FileStorage()
        self.test_file = "file.json"
        self.model = BaseModel()

    def tearDown(self):
        """Clean up resources after each test."""
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects.clear()

    def test_all(self):
        """Test that all() returns the __objects dictionary."""
        self.assertEqual(self.storage.all(), {})
        key = f"BaseModel.{self.model.id}"
        self.storage.new(self.model)
        self.assertIn(key, self.storage.all())

    def test_new(self):
        """Test that new() adds an object to __objects."""
        key = f"BaseModel.{self.model.id}"
        self.storage.new(self.model)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], self.model)

    def test_save(self):
        """Test that save() writes __objects to a file."""
        key = f"BaseModel.{self.model.id}"
        self.storage.new(self.model)
        self.storage.save()
        with open(self.test_file, "r") as f:
            data = json.load(f)
        self.assertIn(key, data)
        self.assertEqual(data[key]["id"], self.model.id)

    def test_reload(self):
        """Test that reload() loads objects from a file."""
        key = f"BaseModel.{self.model.id}"
        self.storage.new(self.model)
        self.storage.save()
        FileStorage._FileStorage__objects.clear()  # Clear objects to ensure reload works
        self.storage.reload()
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].id, self.model.id)

    def test_reload_no_file(self):
        """Test that reload() does nothing if the file does not exist."""
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass
        self.storage.reload()  # Should not raise any exception
        self.assertEqual(self.storage.all(), {})

    def test_file_path(self):
        """Test the __file_path private attribute."""
        self.assertEqual(self.storage._FileStorage__file_path, self.test_file)

    def test_objects_dict(self):
        """Test the __objects private attribute."""
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_invalid_reload(self):
        """Test reload with invalid JSON data."""
        with open(self.test_file, "w") as f:
            f.write("Invalid JSON")
        with self.assertRaises(json.JSONDecodeError):
            self.storage.reload()


if __name__ == "__main__":
    unittest.main()
