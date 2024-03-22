#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_score = 0
    for k, v in a_dictionary.items():
        if best_score < v:
            best_score = v
            best_key = k
    return best_key
