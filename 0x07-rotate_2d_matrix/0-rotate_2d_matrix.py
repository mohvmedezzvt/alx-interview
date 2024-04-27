#!/usr/bin/python3
"""
This module contains a function to rotate a 2D matrix in-place.
"""


def rotate_2d_matrix(matrix: list[list[int]]) -> None:
    """
    Rotate a 2D matrix in-place.

    Args:
        matrix (list[list[int]]): The 2D matrix to rotate.

    Returns:
        None: The function modifies the matrix in-place.

    """
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            # save the topLeft
            topLeft = matrix[top][left + i]

            # move bottom left to top left
            matrix[top][left + i] = matrix[bottom - i][left]

            # move bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # move top right to bottom right
            matrix[bottom][right - i] = matrix[top + i][right]

            # move top left to top right
            matrix[top + i][right] = topLeft

        left += 1
        right -= 1
