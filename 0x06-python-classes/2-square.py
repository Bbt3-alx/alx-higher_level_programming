#!/usr/bin/python3
""" A simple module with a single class """


class Square:
    """ A class Square """
    def __init__(self, size=0):
        """ class initialisation """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
