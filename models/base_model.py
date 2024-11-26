#!/usr/bin/python3
"""Basemodel.py"""
import uuid
from datetime import datetime


class BaseModel:
    """Class BaseModel"""

    def __init__(self):
        """Instantiation."""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """Print the class name and it's dict."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime."""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__."""
        dict1 = self.__dict__.copy()
        dict1["created_at"] = self.created_at.isoformat()
        dict1["updated_at"] = self.updated_at.isoformat()
        dict1["__class__"] = self.__class__.__name__

        return dict1
