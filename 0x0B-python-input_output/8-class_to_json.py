#!/usr/bin/python3
"""Class to JSON"""


import json


def class_to_json(obj):
    """
    function that returns the dictionary description with simple data structure
    """
    json_dict = {}

    # Iyterate over the attributes of the object
    for attr in dir(obj):
        # Skip private attributes and special methods
        if attr.startswith('__'):
            continue

        value = getattr(obj, attr)

        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value

    return json_dict
