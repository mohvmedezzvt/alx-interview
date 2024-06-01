#!/usr/bin/python3
"""This module contains a function to rotate a 2D matrix in-place."""


def rotate_2d_matrix(matrix: list[list[int]]) -> None:
    """
    Rotate a 2D matrix in-place.

    Args:
        matrix (list[list[int]]): The 2D matrix to rotate.

    Returns:
        None: The function modifies the matrix in-place.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
