#!/usr/bin/python3
"""This module contains three function"""

def copy_all(characters, clipboard, operations):
    """
    Method that copies all characters from the characters to the clipboard.
    Args:
        characters: an integer
        clipboard: an integer
    Return: a tuple of integers
    """
    clipboard = characters
    return clipboard, operations + 1

def paste(characters, clipboard, operations):
    """
    Method that pastes all characters from the clipboard to the characters.
    Args:
        characters: an integer
        clipboard: an integer
    Return: a tuple of integers
    """
    characters += clipboard
    return characters, operations + 1

def minOperations(n):
    """
    Method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
    Description: 
        In a text file, there is a single character H.
        Your text editor can execute only two operations in this file:
        Copy All and Paste. Given a number n, write a method that
        calculates the fewest number of operations needed to result
        in exactly n H characters in the file.
    Args: n is an integer
    Return: an integer
    """
    operations = 0
    characters = 1
    clipboard = 0

    while characters < n:
        # copy when n is divisible by characters
        if n % characters == 0:
            clipboard, operations = copy_all(characters, clipboard, operations)
            characters, operations = paste(characters, clipboard, operations)
        else:
            # paste when n is not divisible by characters
            characters, operations = paste(characters, clipboard, operations)
    return operations