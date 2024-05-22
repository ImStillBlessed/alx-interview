#!/usr/bin/python3
"""
This module contains a function that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    returns: True if data is a valid UTF-8 encoding, False otherwise.
    """
    num_bytes = 0

    for num in data:
        mask = 1 << 7
        if not num_bytes:
            while mask & num:
                num_bytes += 1
                mask = mask >> 1

            if not num_bytes:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if num >> 6 != 0b10:
                return False

        num_bytes -= 1

    return num_bytes == 0