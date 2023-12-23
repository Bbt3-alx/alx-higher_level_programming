#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value_int = int(value)
        print("{:d}".format(value_int))
        return True
    except:
        return False
