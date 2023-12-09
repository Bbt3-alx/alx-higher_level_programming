#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = [x for x in my_list if my_list.count(x) == 1]
    return sum(new_list)
