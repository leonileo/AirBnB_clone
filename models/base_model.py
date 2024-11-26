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
        dict1 = self.__dict__.copy()
        dict1["created_at"] = self.created_at
        dict1["updated_at"] = self.updated_at
        dict1["__class__"] = self.__class__.__name__
        
        return dict1

m = BaseModel()
