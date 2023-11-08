#!/usr/bin/python3
"""returns a list of lists of integers"""


def pascal_triangle(n):
    """returns an empty list"""
    if n <= 0:
        return []

    def generate_row(prev_row):
        """returns a triangle"""
        if not prev_row:
            return [1]
        new_row = [1]
        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i - 1] + prev_row[i])
        new_row.append(1)
        return new_row

    triangle = []
    row = []
    for _ in range(n):
        row = generate_row(row)
        triangle.append(row)

    return triangle
