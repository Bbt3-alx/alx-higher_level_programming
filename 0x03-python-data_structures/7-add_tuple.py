#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    r = (int(tuple_a[0]) + int(tuple_b[0]), int(tuple_a[1]) + int(tuple_b[1]))
    return r
