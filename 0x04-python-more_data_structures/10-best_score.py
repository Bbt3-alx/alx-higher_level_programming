#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    best_score = float('-inf')
    best_key = None
    for k, v in a_dictionary.items():
        if best_score < v:
            best_score = v
            best_key = k
    return best_key
