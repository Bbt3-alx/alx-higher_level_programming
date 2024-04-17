#!/usr/bin/python3
"""
This check if an object is an instance of or if
the object is an instance of a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    args:
        obj: an object
        a_clas: a class
    Return: a boolean
    """
    if isinstance(obj, a_class):
        return True
    return False
