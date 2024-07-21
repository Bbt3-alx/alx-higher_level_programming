#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    args:
        n - NUmber of row
    """

    triangle = [[1]]

    if n <= 0:
        return []

    for i in range(1, n):
        new_row = [1]
        prev_row = triangle[-1]

        for j in range(1, i):
            new = prev_row[j - 1] + prev_row[j]
            new_row.append(new_element)

        new_row.append(1)
        triangle.append(new_row)

    return triangle
