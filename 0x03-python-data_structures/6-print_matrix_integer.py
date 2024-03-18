#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for element in matrix:
        for x in element:
            print("{:d}".format(x), end=' ')
        print()
