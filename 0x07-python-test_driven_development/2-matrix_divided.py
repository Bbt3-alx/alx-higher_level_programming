#!/usr/bin/pyrthon3
""" A module with a function that devides elements of a matrix"""


def matrix_divided(matrix, div):
    """ a function that divides all elements of a matrix """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    new_list = []
    if not isinstance(matrix, list):
        raise TypeError(msg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrix_len = len(matrix[0])

    for element in matrix:
        if len(element) != matrix_len:
            raise TypeError("Each row of the matrix must have the same size")
        else:
            for row in element:
                if not isinstance(row, (int, float)):
                    raise TypeError(msg)
                else:
                    new_list.append(round(row / div, 2))
    return new_list
