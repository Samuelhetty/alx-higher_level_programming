#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for aa i range(1, 3):
        try:
            if aa > a:
                raise Exception('Too far')
            else:
                result += a ** b / aa
        except Exception:
            result = b + a
            break
    return result
