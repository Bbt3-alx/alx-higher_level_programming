#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{:s}".format(chr(ord(c) - 32)) if 'a' <= c <= 'z'
            else "{:s}".format(c), end='')
    print()