#!/usr/bin/python3
""" This module have a function that prints a text with 2 new line after
each '.? and :'
"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines after each of these
    characters: ., ? and :

    args:
        text - A string to printed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    cleaned_text = text.strip()

    for char in cleaned_text:
        if char not in ".?:":
            print(char, end='')
        else:
            print(char)
            print()
