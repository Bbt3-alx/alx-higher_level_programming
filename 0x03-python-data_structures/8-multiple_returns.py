#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        first_char = None
        s_len = 0
    else:
        first_char = sentence[0]
        s_len = len(sentence)
    return s_len, first_char
