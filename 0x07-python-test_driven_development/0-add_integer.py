#!/usr/bin/python3
"""This module have a function that add integer"""


def add_integer(a, b=98):
    """A function that adds 2 integer and return the result"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
