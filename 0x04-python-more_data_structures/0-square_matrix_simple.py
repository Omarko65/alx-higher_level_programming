#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = 0
    b = 0
    c = []
    for a in range(3):
        d=[]
        for b in range(3):
            d.append(matrix[a][b] ** 2)
            b += 1
        a = a + 1
        c.append(d)
    return c

