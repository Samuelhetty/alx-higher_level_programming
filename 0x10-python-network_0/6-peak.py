#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None

    first_hf = len(list_of_integers)
    mid = int(first_hf / 2)

    if mid -1 < 0 and mid + 1 >= first_hf:
        return list_of_integers[mid]
    elif mid - 1 < 0:
        return list_of_integers[mid] if list_of_integers[mid] >\
                list_of_integers[mid + 1] else list_of_integers[mid + 1]
    elif mid + 1 >= first_hf:
        return list_of_integers[mid] if list_of_integers[mid] >\
                list_of_integers[mid - 1] else list_of_integers[mid - 1]

    if list_of_integers[mid - 1] < list_of_integers[mid] > list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if list_of_integers[mid + 1] > list_of_integers[mid - 1]:
        return find_peak(list_of_integers[mid:])
    return find_peak(list_of_integers[:mid])
