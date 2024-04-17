#!/usr/bin/python3
"""Return True or False """


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of
    the specified class ; otherwise False

    args:
        obj - an object
        a_class - a class
    Return: True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
