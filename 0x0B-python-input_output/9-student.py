#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """Instantiate the class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        json_data = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }

        return json_data
