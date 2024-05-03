#!/usr/bin/python3
"""this mdoule contains one function"""

def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened.
    Args: boxes is a list of lists
    Return: True if all boxes can be opened, else return False
    """
    keys = {0}
    opened_boxes = {0}
    while keys:
        box = keys.pop()
        for key in boxes[box]:
            if key not in opened_boxes:
                keys.add(key)
                opened_boxes.add(key)
    return len(opened_boxes) == len(boxes)
