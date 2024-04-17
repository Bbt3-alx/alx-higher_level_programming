#!/usr/bin/python3
"""
Check for a class inheritances
"""


def inherits_from(obj, a_class):
    """
     returns True if the object is an instance of a class that inherited
     (directly or indirectly) from the specified class ; otherwise False.

     args:
        obj: an object ex: int, float or True
        a_class: a class
    return: A Boolean
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
