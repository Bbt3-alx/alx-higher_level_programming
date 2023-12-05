#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 1:
        tuple_a_first = 0
    else:
        tuple_a_first = tuple_a[0]

    if len(tuple_b) < 1:
        tuple_b_first = 0
    else:
        tuple_b_first = tuple_b[0]

    if 2 > len(tuple_a):
        tuple_a_second = 0
    else:
        tuple_a_second = tuple_a[1]
    if len(tuple_b) < 2:
        tuple_b_second = 0
    else:
        tuple_b_second = tuple_b[1]

    tuples = (tuple_a_first + tuple_b_first, tuple_a_second + tuple_b_second)
    return tuples
