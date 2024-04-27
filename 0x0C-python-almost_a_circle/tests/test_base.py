#!/usr/bin/python3
"""Test base"""


import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test the Base class"""
    def test_to_json_string_empty_list(self):
        """Test to json string empty list"""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_non_empty_list(self):
        """Test to json string non empty list"""
        list_dicts = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        json_string = Base.to_json_string(list_dicts)
        expected_json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        self.assertEqual(json_string, expected_json_string)

    def test_save_to_file(self):
        """Test save to file"""
        list_objs = [Base(1), Base(2)]
        Base.save_to_file(list_objs)
        self.assertTrue(os.path.exists("Base.json"))
        with open("Base.json", "r") as file:
            json_data = file.read()
            self.assertEqual(json_data, '[{"id": 1}, {"id": 2}]')

    def tearDown(self):
        """ tear down """
        if os.path.exists("Base.json"):
            os.remove("Base.json")


if __name__ == '__main__':
    unittest.main()
