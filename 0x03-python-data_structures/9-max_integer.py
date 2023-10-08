#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    cont = my_list[0]
    for aa in my_list:
        if aa > cont:
            cont = aa
    return cont
