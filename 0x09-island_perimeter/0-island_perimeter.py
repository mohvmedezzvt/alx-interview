#!/usr/bin/python3
"""Module for island_perimeter"""


def island_perimeter(grid):
    """
    Function that returns the perimeter of the island described in grid
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check the cell above
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                # Check the cell below
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                # Check the cell to the left
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                # Check the cell to the right
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
