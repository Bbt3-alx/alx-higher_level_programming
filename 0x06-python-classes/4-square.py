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

    @property
    def size(self):
        """Retrieve the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Set a value to the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValuError("size must be >= 0")
        self__size = value

    def area(self):
        """ return the current square area """
        return self.__size ** 2
