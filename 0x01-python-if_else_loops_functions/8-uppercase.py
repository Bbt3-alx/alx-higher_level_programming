#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for s in str:
        if ('a' <= s <= 'z'):
            new_str += chr(ord(s) - 32)
        else:
            new_str += s
    return new_str
