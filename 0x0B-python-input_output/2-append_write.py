#!/usr/bin/python3

""" Module that appends at the end of a text file"""


def append_write(filename="", text=""):
    """
    A function that appends a string at the end of
    a file and returns the number of character added
    args:
        filename - The name of the text file
        text - The text to be append in the filename

    Return: The number of characters added
    """

    with open(filename, 'a') as f:
        data = f.write(text)

    return data
