#!/usr/bin/python3
'''module definition of a function that divides matrix'''


def matrix_divided(matrix, div):
    '''function definition of matrix divided'''

    a = 0
    b = 0
    c = []
    row = len(matrix)
    col = len(matrix[0])
    i = 0

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) not in [list]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(matrix[i]) not in [list] or type(matrix[i + 1]) not in [list]:
        raise TypeError("_matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix[i]) != len(matrix[i + 1]):
        raise TypeError("Each row of the matrix must have the same size")

    for a in range(row):
        d = []
        for b in range(col):
            if type(matrix[a][b]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            k = matrix[a][b] / div
            d.append(round(k, 2))
            b = b + 1
        a = a + 1
        c.append(d)
    return c
