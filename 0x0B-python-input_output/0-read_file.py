#!/usr/bin/python3
""" Module that read a text file """


def read_file(filename=""):
    """
    A function that reads a text file (UTF-8) and prints it to stdout
    Args:
        filename - The text file to read
    Return: Nothin
    """
    with open(filename, 'r') as f:
        text = f.read()
        print(text, end='')
