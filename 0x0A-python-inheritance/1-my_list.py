#!/usr/bin/python3
"""
A module with a class that inherit from list
"""


class MyList(list):
    """A class that inherit from list"""
    def print_sorted(self):
        """A public method that print the sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
