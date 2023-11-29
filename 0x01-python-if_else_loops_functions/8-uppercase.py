#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for s in str:
        if (s.isalpha):
            new_str += chr(ord(s) - 32) if ('a' <= s <= 'z') else s
            print("{}".format(new_str))
        else:
            new_str += s
            print("{}".format(new_str))
