#!/usr/bin/python3
"""reads text file"""

def read_file(filename=""):
    """reads text file"""
    with open(filename, mode='r', encoding='utf-8') as a_file:
        print(a_file.read(), end='')
        a_file.close()
