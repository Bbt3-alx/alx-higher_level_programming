#!/usr/bin/python3
"""A module that import a class from another module"""


class BaseGeometry:
    """a class BaseGeometry (based on 5-base_geometry)"""
    def area(self):
        """Raise a simple exception"""
        raise Exception("area() is not implemented")
