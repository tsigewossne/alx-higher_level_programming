#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for ind in set(my_list):
        add = ind + add
        return (add)
