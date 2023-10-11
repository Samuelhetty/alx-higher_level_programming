#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = {ky: val for ky, val in a_dictionary.items() if val == value}
    for key in new:
        a_dictionary.pop(key)
        return a_dictionary
