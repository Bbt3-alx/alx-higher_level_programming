#!/usr/bin/python3
""" This module have a function that print a sentence with the
name and the first name"""


def say_my_name(first_name, last_name=""):
    """
    This function print `My name is <first name> <last name>

    args:
        first_name : The first name
        last_name : The last name
    return nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
