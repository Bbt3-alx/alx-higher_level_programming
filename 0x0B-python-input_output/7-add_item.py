#!/usr/bin/python3
"""Load, add, save"""


import json
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """adds all arguments to a Python list, and then save them to a file"""

    filename = "add_item.json"

    # Load existing data if file exists

    if os.path.exists(filename):
        json_list = load_from_json_file(filename)
    else:
        json_list = []

    # Add command-line arguments to the list
    json_list.extend(sys.argv[1:])

    # Save the update list to the file
    save_to_json_file(json_list, filename)


if __name__ == "__main__":
    main()
