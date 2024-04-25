#!/usr/bin/python3
"""This module will contain the base class of all other class in this class"""


import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                json.write([])
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))
