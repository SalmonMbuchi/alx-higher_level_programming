#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix.append(i,j**2)
    return new_matrix
