#!/usr/bin/python3
"""N queens puzzle

This script solves the N queens puzzle,
which is a classic problem in chess.
The goal is to place N queens on an N x N chessboard
such that no two queens threaten each other.
In other words, no two queens can share the same row, column, or diagonal.

The script takes a single command-line argument, N, which represents the
size of the chessboard and the number of queens to be placed.
It then generates and prints all possible solutions to the puzzle.

Usage: ./0-nqueens.py N

Example:
    $ ./0-nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]

    $ ./0-nqueens.py 6
    [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
    [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
    [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
    [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
"""

import sys


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)

    col = set()
    posDiag = set()  # (r + c)
    negDiag = set()  # (r - c)
    res = []
    board = [['.'] * N for i in range(N)]

    def backtrack(r):
        if r == N:
            queens = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 'Q':
                        queens.append([i, j])
            res.append(queens)
            return

        for c in range(N):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = 'Q'

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = '.'

    backtrack(0)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
