#!/usr/bin/python3
"""Basemodel.py"""
import uuid
from datetime import datetime


class BaseModel:
    """Class BaseModel"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__."""
        return self.__dict__

m = BaseModel()
