#!/usr/bin/python3
"""appends text to input file"""


def append_write(filename="", text=""):
    """appends text to input file"""
    chars_written = 0
    with open(filename, mode='a', encoding='utf-8') as f_io:
        chars_written += f_io.write(text)
        f_io.close()
    return chars_written
