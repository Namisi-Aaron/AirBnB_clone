#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
"""This module contains the definition of the BaseModel class"""


class BaseModel:
    """Defines the class BaseModel"""
    def __init__(self, *args, **kwargs):
        """Is the initialization method for the BaseModel class"""
        if kwargs:
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if 'updated_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                        kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints [<class name>] (<self.id>) <self.__dict__>"""
        return '[{}] ({}) ({})'.format(self.__class__.__name__,
                                       self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        new_dict = self.__dict__
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
