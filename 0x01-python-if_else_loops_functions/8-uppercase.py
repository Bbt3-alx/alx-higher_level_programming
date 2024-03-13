#!/usr/bin/python3
def uppercase(str):
    for c in str:
        v = 'a' <= c <= 'z'
        print('{}'.format(chr(ord(c) - 32)) if v else '{}'.format(c), end='')
    print()
