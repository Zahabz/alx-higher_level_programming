#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    new_matrix = [[x ** 2 for x in rows] for rows in matrix]
    return new_matrix
