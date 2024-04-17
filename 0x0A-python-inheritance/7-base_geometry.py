#!/usr/bin/python3
"""A module with a class named BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """Raise an Exception with a message"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
