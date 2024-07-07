#!/usr/bin/python3
''' Module to do some N queens puzzle Challenge. '''

import sys

def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(row, col, solution):
        for r, c in solution:
            if r == row or c == col or r + c == row + col or r - c == row - col:
                return False
        return True

    def solve(row, solution):
        if row == N:
            print(solution)
            return
        for col in range(N):
            if is_safe(row, col, solution):
                solve(row + 1, solution + [(row, col)])

    solve(0, [])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(N)