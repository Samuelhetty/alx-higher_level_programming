#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[row[aa]**2 for aa in range(len(row))] for row in matrix]
