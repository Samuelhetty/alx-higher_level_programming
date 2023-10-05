#!/usr/bin/python3
from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""

    if a < b:
        c = add(a, b)
        for aa in range(4, 6):
            c = add(c, aa)
        return (c)
    else:
        return(sub(a, b))
