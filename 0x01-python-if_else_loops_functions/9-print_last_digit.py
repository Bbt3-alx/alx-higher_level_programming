#!/usr/bin/python3
def print_last_digit(number):
    abs_value = abs(number)
    last_d = abs_value % 10
    print(last_d, end='')
    return last_d
