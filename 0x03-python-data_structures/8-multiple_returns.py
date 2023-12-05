#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence is None):
        first_char = None
        str_len = 0
    else:
        str_len = len(sentence)
        first_char = sentence[0]
    return str_len, first_char
