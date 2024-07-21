#!/usr/bin/python3
"""student to disk and reload"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of the class student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        json_data = {}

        if attrs is None:
            json_data = {
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'age': self.age
                    }
        else:
            for attribute in attrs:
                if hasattr(self, attribute):
                    json_data[attribute] = getattr(self, attribute)

        return json_data

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""

        for k, v in json.items():
            setattr(self, k, v)
