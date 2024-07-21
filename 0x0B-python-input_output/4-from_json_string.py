#!/usr/bin/python3
"""A module that deserialize"""


import json


def from_json_string(my_str):
    """
    A function that returns an object (Python data structure)
    represented by a JSON string"
    args:
        my_str - json string to convert
    """

    my_obj = json.loads(my_str)
    return my_obj
