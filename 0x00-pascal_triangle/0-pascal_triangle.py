#!/usr/bin/python3
"""
0-pascal_triangle - representing the Pascal’s triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []

    if n <= 0:
        return triangle

    for row_num in range(n):
        row = []

        for i in range(row_num + 1):
            if i == 0 or i == row_num:
                row.append(1)
            else:
                value = triangle[row_num - 1][i - 1] + triangle[row_num - 1][i]
                row.append(value)

        triangle.append(row)

    return triangle
