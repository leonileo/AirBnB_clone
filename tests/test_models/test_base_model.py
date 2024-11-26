#!/usr/bin/python3
"""Test for base_model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):

    def test_instantiation(self):
        """Test the attributes when the instance is created."""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)

    def test_unique_id(self):
        """Test if the created instances has a unique ID."""
        b1 = BaseModel()
        b2 = BaseModel()
        
        self.assertNotEqual(b1.id, b2.id)

    def test_str(self):
        """Test the string representation method."""
        base = BaseModel()
        strp = "[{}] ({}) {}".format(base.__class__.__name__, base.id, base.__dict__)

        self.assertEqual(str(base), strp)

    def test_save_method(self):
        """ Test if the save method updated the updated_at attribute."""
        base = BaseModel()
        up = base.updated_at
        base.save()

        self.assertNotEqual(up, base.updated_at)
        self.assertGreater(base.updated_at, up)

    def test_to_dict(self):
        """Test the dict method"""
        base = BaseModel()
        bdict = base.to_dict()

        self.assertEqual(bdict["__class__"], "BaseModel")
        self.assertEqual(bdict["id"], base.id)
        self.assertEqual(bdict["created_at"], base.created_at.isoformat())
        self.assertEqual(bdict["updated_at"], base.updated_at.isoformat())

    def test_to_dict_types(self):
        """Test if to_dict returns string format for datetime."""
        base = BaseModel()
        bdict = base.to_dict()

        self.assertIsInstance(bdict["created_at"], str)
        self.assertIsInstance(bdict["updated_at"], str)

    def test_save_updates_only_updated_at(self):
        """Checks if save obly updates the updated_at attribute."""
        base = BaseModel()
        b_created_at = base.created_at
        base.save()
        self.assertEqual(base.created_at, b_created_at)


if __name__ == "__main__":
    unittest.main()
