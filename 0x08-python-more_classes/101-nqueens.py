#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    for i in range(col):
        if board[row][i]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, len(board), -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_nqueens(N):
    """
    Solve the N Queens problem
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def solve(col):
        if col >= N:
            solution = []
            for row in range(N):
                for col in range(N):
                    if board[row][col] == 1:
                        solution.append([row, col])
            solutions.append(solution)
            return

        for row in range(N):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(col + 1)
                board[row][col] = 0

    solve(0)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
