#!/usr/bin/python3
"""This module will contain the base class of all other class in this class"""


class Base:
    """The “base” class of all other classes in this project."""
    __nb_objects = 0
    def __init__(self, id=None):
        """Class initialization"""
        if id is not None:
            self._id = id
        else:
            Base.__nb_objects += 1
            self._id = Base.__nb_objects

    @property
    def id(self):
        """Get the id"""
        return self._id

    @id.setter
    def id(self, value):
        """Set the id"""
        if value is not None and isinstance(value, int):
            self._id = value
