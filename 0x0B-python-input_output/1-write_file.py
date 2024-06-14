#!/usr/bin/python3

def write_file(filename="", text=""):
    """
        This function writes a string to a text file
        and returns the number of characters writen
        Args:
            filename - the name of the file to write
        Return : The number of characters written
    """

    with open(filename, 'w') as f:
        data = f.write(text)

    return data
