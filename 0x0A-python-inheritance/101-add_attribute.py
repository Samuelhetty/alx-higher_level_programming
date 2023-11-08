#!/usr/bin/python3
"""Module to adds a new attribute to an object if it’s possible"""

def add_attribute(obj, attr_name, attr_value):
    """adds a new attribute to an object"""
    if hasattr(obj, attr_name):
        raise TypeError("Can't add a new attribute")
    else:
        setattr(obj, attr_name, attr_value)
