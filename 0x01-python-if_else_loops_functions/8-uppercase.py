#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 'a' <= c <= 'z':
            print("{:s}".format(chr(ord(c) - 32)), end='')
        else:
            print("{:s}".format(c), end='')
    print()
