#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        my_list = []
    for i in range(1, len(my_list) + 1):
        if isinstance(i, int):
            print("{:d}".format(my_list[-i]))
