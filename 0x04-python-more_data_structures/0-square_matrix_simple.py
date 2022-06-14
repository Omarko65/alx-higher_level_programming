#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = 0
    b = 0
    c = []
    row = len(matrix)
    col = len(matrix[0])
    for a in range(row):
        d = []
        for b in range(col):
            d.append(matrix[a][b] ** 2)
            b = b + 1
        a = a + 1
        c.append(d)
    return c
