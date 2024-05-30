#!/usr/bin/python3
"""
Module contains the n-queens problem solution.
"""

import sys


def print_usage_and_exit():
    """Print usage message and exit."""
    print("Usage: nqueens N")
    sys.exit(1)


def print_number_error_and_exit():
    """Print number error message and exit."""
    print("N must be a number")
    sys.exit(1)


def print_minimum_error_and_exit():
    """Print minimum error message and exit."""
    print("N must be at least 4")
    sys.exit(1)


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].

    Args:
        board (list): The current state of the board.
        row (int): The row index.
        col (int): The column index.

    Returns:
        bool: True if it's safe, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """
    Solve the N queens problem.

    Args:
        N (int): The size of the board (N x N).

    Returns:
        list: A list of solutions, where each solution is represented as
              a list of column indices for each row.
    """
    def solve(row, board):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1, board)
                board[row] = -1

    solutions = []
    solve(0, [-1] * N)
    return solutions


def main():
    """Main function to parse input and solve the N queens problem."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_number_error_and_exit()

    if N < 4:
        print_minimum_error_and_exit()

    solutions = solve_nqueens(N)
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(N)]
        print(formatted_solution)


if __name__ == "__main__":
    main()
