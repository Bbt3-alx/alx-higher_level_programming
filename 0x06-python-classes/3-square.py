#!/usr/bin/python3
""" A module that contain a class """
class Square:
    """ a class Square that defines a square """
    def __init__(self, size=0):
        """ class initialisation """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Return the current square area """
        return self.__size ** 2
