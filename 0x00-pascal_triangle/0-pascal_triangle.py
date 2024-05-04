#!/usr/bin/python3
"""
This module contains one function
"""

def pascal_triangle(n):
    """
    This function returns a list of lists of integers
    representing the Pascal’s triangle of n
    Returns: an empty list if n <= 0
    """
    triangle = []
    for row in range(n):
        current_row = [1]

        if row > 0:
            prev_row = triangle[row - 1]
            for i in range(len(prev_row) - 1):
                new_value = prev_row[i] + prev_row[i + 1]
                current_row.append(new_value)

            current_row.append(1)

        triangle.append(current_row)

    return triangle
