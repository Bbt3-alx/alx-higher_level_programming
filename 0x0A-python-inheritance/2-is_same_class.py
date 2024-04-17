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
    if type(obj) is a_class:
        return True
    return False
