#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of the class Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """retrieves a dictionary representation of a Student instance"""

        json_data = {}

        if attr is None:
            json_data = {
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "age": self.age
                    }
        else:
            for i in attr:
                if hasattr(self, i):
                    json_data[i] = getattr(self, i)

        return json_data
