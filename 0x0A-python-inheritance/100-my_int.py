#!/usr/bin/python3
"""Module of a class MyInt that inherits from int"""


class MyInt(int):
    """class to override int comparisons"""
    def __eq__(self, other):
        return int(self) != int(other)

    def __ne__(self, other):
        return int(self) == int(other)
