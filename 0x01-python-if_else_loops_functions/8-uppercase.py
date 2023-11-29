#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for s in str:
        if ('a' <= s <= 'z'):
            new_str += chr(ord(s) - 32)
            print("{}".format(new_str))
        else:
            new_str += s
            print("{}".format(new_str))
