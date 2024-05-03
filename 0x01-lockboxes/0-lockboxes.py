#!/usr/bin/env python3
"""this mdoule contains one function"""

def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened.
    args: boxes is a list of lists
    Return: True if all boxes can be opened, else return False
    """
    keys = [0]
    for open_box in keys:
        if len(keys) == len(boxes):
            return True
        for key in boxes[open_box]:
            if key not in keys:
                keys.append(key)
    if len(keys) == len(boxes):
        return True
    return False
