#!/usr/bin/python3
"""Load a JSON file"""


import json


def load_from_json_file(filename):
    """A function that creates an Object from a 'JSON file'"""

    with open(filename, 'r') as f:
        my_data = json.load(f)

    return my_data
