#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                 'D': 500, 'M': 1000}

    total = 0
    old_val = 0

    for char in reversed(roman_string):
        if char not in roman_num:
            return 0

        curr_val = roman_num[char]

        if curr_val < old_val:
            total -= curr_val
        else:
            total += curr_val
        old_val = curr_val

    return total
