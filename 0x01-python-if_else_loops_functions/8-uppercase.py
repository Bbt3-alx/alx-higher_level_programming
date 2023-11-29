#!/usr/bin/python3
def uppercase(str):
    new_str = ""

    for s in str:
        if (s.isalpha):
            new_str += chr(ord(s) - 32) if ('a' <= s <= 'z') elses
        else:
            new_str += s
        print("{}".format(new_str))
