#!/usr/bin/python3
"""
A module that print all the available attributes and methods of an object
"""


def lookup(obj):
    """
    This function return the list of available attributes
    and methods of an object
    args:
        obj - oject

    Return: a list with available attributes and methods of obj
    """
    return dir(obj)
