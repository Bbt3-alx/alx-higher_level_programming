#!/usr/bin/python3
"""A module with a single class its attribute"""


class Square:
    """a class Square that defines a square"""
    def __init__(self, size=0):
        """Initialisation of the class"""
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def size(self):
        """Retrieve the size value"""
        return self.__size

    def size(self, value):
        """ Set a value to the size"""
        self.value = value

    def area(self):
        """ return the current square area """
        return self.__size ** 2
