#!/usr/bin/python3
"""This module serialize an objetc"""


import json


def to_json_string(my_obj):
    """
    This  function that returns the JSON representation of an object (string)
    args:
        my_obj - the objet to serialize
    """
    json_str = json.dumps(my_obj)
    return json_str
