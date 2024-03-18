#!/usr/bin/env python3
""" Lockboxes """

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all the boxes can be opened.

    This function takes a list of lists, where each inner list represents a box
    and contains the indices of the boxes that can be opened
    with the corresponding key.

    Args:
        boxes (List[List[int]]): A list of lists representing the boxes
        and their keys.

    Returns:
        bool: True if all the boxes can be opened, False otherwise.

    Examples:
        >>> boxes = [[1], [2], [3], []]
        >>> canUnlockAll(boxes)
        True

        >>> boxes = [[1, 2], [3], [4], []]
        >>> canUnlockAll(boxes)
        True

        >>> boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
        >>> canUnlockAll(boxes)
        False
    """
    if len(boxes) == 0:
        return False

    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)

    if len(keys) == len(boxes):
        return True

    return False
