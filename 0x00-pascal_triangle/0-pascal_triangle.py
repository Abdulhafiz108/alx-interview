#!/usr/bin/python3
"""
A file cotaining my pascal's triangle funcion
"""


def pascal_triangle(n):
    """
    A function that returns a list of Pascal’s triangle
    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)

    return triangle
