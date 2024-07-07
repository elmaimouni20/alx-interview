#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./0-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys

def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)

def print_error_and_exit(message):
    print(message)
    sys.exit(1)

def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n):
    def solve(row, board):
        if row == n:
            solutions.append(board[:])
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve(row + 1, board)
                board[row] = -1

    solutions = []
    board = [-1] * n
    solve(0, board)
    return solutions

def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print_error_and_exit("N must be a number")
    
    if n < 4:
        print_error_and_exit("N must be at least 4")

    solutions = solve_nqueens(n)
    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])

if __name__ == "__main__":
    main()